# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "playwright>=1.45.0",
#   "anthropic>=0.30.0",
#   "python-dotenv>=1.0.0",
#   "markdown>=3.5.0",
# ]
# ///
"""
Optilogic リリースログ 通知スクリプト
使い方:
  uv run notifier.py --setup   # 初回のみ: ブラウザでログイン → セッション保存
  uv run notifier.py           # リリースログ確認・翻訳・メール通知（定期実行用）
  uv run notifier.py --check   # 通知なしで最新内容を確認するだけ
"""

import hashlib
import os
import smtplib
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import anthropic
import markdown
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Windowsコンソール(cp932)で絵文字等を扱えるようにする
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# --- パス設定 ---
BASE_DIR = Path(__file__).parent
ENV_FILE = BASE_DIR / ".env"
SESSION_FILE = BASE_DIR / "session.json"
LAST_HASH_FILE = BASE_DIR / "last_hash.txt"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

RELEASE_LOG_URL = "https://optilogic.app/#/release-log"
# ----------------

load_dotenv(ENV_FILE)

# 挨拶文は環境変数から取得（GitHub Secrets: EMAIL_GREETING）
EMAIL_GREETING = os.getenv(
    "EMAIL_GREETING",
    "Optilogicの最新リリースログが更新されましたのでお知らせいたします。",
)


# ── セッション管理 ──────────────────────────────────────────────

def setup_session():
    """初回セットアップ: 可視ブラウザでログインしてセッションを保存する"""
    print("=" * 60)
    print("【初回セットアップ】")
    print("ブラウザが開きます。Optilogicにログインしてください。")
    print("ログイン後、リリースログページ（#/release-log）が表示されたら")
    print("このターミナルに戻ってEnterを押してください。")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        page.goto(RELEASE_LOG_URL)
        input("\n>>> ログイン完了後、Enterを押してください: ")
        context.storage_state(path=str(SESSION_FILE))
        print(f"[OK] セッションを保存しました: {SESSION_FILE}")
        browser.close()


# ── コンテンツ取得 ───────────────────────────────────────────────

def _do_login(page, email: str, password: str):
    """メール・パスワードでOptilogicにログインする（GitHub Actions用）"""
    # メールアドレス入力
    page.wait_for_selector(
        "input[type='email'], input[name='email'], input[name='username']",
        timeout=15_000,
    )
    email_input = page.locator(
        "input[type='email'], input[name='email'], input[name='username']"
    ).first
    email_input.fill(email)

    # Auth0等の2段階ログイン（Continueボタンがある場合はEnterで進む）
    email_input.press("Enter")
    page.wait_for_timeout(2_000)

    # パスワード入力
    pw = page.locator("input[type='password']").first
    pw.wait_for(timeout=10_000)
    pw.fill(password)

    # Enterキーでフォーム送信（ボタンのセレクタに依存しない）
    pw.press("Enter")

    # ログイン完了を最大30秒待つ
    for _ in range(15):
        page.wait_for_timeout(2_000)
        if "login" not in page.url and "auth" not in page.url:
            print("  ログイン完了")
            return
    raise RuntimeError("ログインがタイムアウトしました。OPTILOGIC_EMAIL/PASSWORDを確認してください。")


def fetch_release_log() -> str:
    """リリースログページを取得してテキストを返す。
    - session.json が存在する場合: セッションを使用（ローカル実行）
    - OPTILOGIC_EMAIL/PASSWORD が設定されている場合: 毎回ログイン（GitHub Actions）
    """
    use_session = SESSION_FILE.exists()
    optilogic_email = os.getenv("OPTILOGIC_EMAIL", "")
    optilogic_password = os.getenv("OPTILOGIC_PASSWORD", "")
    use_credentials = bool(optilogic_email and optilogic_password)

    if not use_session and not use_credentials:
        raise FileNotFoundError(
            "認証情報が見つかりません。\n"
            "ローカル実行時: uv run notifier.py --setup を実行してください。\n"
            "GitHub Actions: OPTILOGIC_EMAIL / OPTILOGIC_PASSWORD を Secrets に設定してください。"
        )

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = (
            browser.new_context(storage_state=str(SESSION_FILE))
            if use_session
            else browser.new_context()
        )
        page = context.new_page()

        print(f"ページ取得中: {RELEASE_LOG_URL}")
        page.goto(RELEASE_LOG_URL, wait_until="domcontentloaded", timeout=45_000)

        # SPAのレンダリング完了を待つ
        try:
            page.wait_for_load_state("networkidle", timeout=15_000)
        except PlaywrightTimeout:
            print("  [警告] ネットワーク待機タイムアウト。取得を継続します。")

        page.wait_for_timeout(2_000)

        # ログイン画面にリダイレクトされた場合
        current_url = page.url
        if "login" in current_url or "auth" in current_url:
            if use_credentials:
                print("  認証情報でログイン中...")
                _do_login(page, optilogic_email, optilogic_password)
                page.goto(RELEASE_LOG_URL, wait_until="domcontentloaded", timeout=45_000)
                try:
                    page.wait_for_load_state("networkidle", timeout=15_000)
                except PlaywrightTimeout:
                    pass
                page.wait_for_timeout(2_000)
            else:
                browser.close()
                raise RuntimeError(
                    "セッションが期限切れです。--setup を再実行してください。"
                )

        # リリースログのテキストを抽出（複数のセレクタを試みる）
        content = ""
        selectors = [
            "[class*='release']",
            "[class*='changelog']",
            "[class*='log']",
            "main",
            "[role='main']",
            ".content",
            "#content",
            "body",
        ]
        for selector in selectors:
            try:
                el = page.locator(selector).first
                text = el.inner_text(timeout=3000)
                if text and len(text.strip()) > 100:
                    content = text.strip()
                    print(f"  コンテンツ取得: セレクタ '{selector}' ({len(content)} 文字)")
                    break
            except Exception:
                continue

        if not content:
            # フォールバック: ページ全体のテキスト
            content = page.inner_text("body")
            print(f"  コンテンツ取得: body全体 ({len(content)} 文字)")

        browser.close()
        return content


# ── 変更検知 ────────────────────────────────────────────────────

def get_content_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()


def load_last_hash() -> str:
    if LAST_HASH_FILE.exists():
        return LAST_HASH_FILE.read_text(encoding="utf-8").strip()
    return ""


def save_current_hash(hash_value: str):
    LAST_HASH_FILE.write_text(hash_value, encoding="utf-8")


def save_log(content: str, translated: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = LOG_DIR / f"release_{timestamp}.md"
    log_file.write_text(
        f"# Optilogic リリースログ取得: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        f"## 日本語訳\n\n{translated}\n\n"
        f"---\n\n## 原文\n\n```\n{content[:5000]}\n```\n",
        encoding="utf-8",
    )
    print(f"[OK] ログ保存: {log_file}")
    return log_file


# ── Claude による翻訳 ────────────────────────────────────────────

def translate_with_claude(raw_content: str) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()

    prompt = f"""以下はOptilogic（CosmicFrog / DataStar / Ada / Composable Apps）の
リリースログページから取得したテキストです。

新しいバージョン・アップデート情報を日本語に翻訳し、以下のフォーマットで整理してください：

---
# Optilogic 最新アップデート情報

（バージョンごとに、追加機能・修正・改善をまとめてください）
---

取得テキスト:
{raw_content[:8000]}
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


# ── メール送信 ───────────────────────────────────────────────────

def send_email(subject: str, body: str):
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASS", "")
    to_addr   = os.getenv("NOTIFY_TO", "")

    if not smtp_user or not smtp_pass:
        print("[警告] SMTP_USER / SMTP_PASS が未設定のためメール送信をスキップします。")
        print("  .env ファイルに設定してください。")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_addr

    # 冒頭の挨拶文（区切り線より前）と本文を分けて装飾する
    parts = body.split("\n\n---\n\n", 1)
    if len(parts) == 2:
        greeting_md, content_md = parts
    else:
        greeting_md, content_md = "", body

    greeting_html = markdown.markdown(greeting_md, extensions=["nl2br"]) if greeting_md.strip() else ""
    content_html = markdown.markdown(content_md, extensions=["tables", "fenced_code", "nl2br"])

    greeting_block = (
        f'<div class="greeting">{greeting_html}</div>' if greeting_html else ""
    )

    html_body = f"""\
<html>
  <head>
    <style>
      body {{
        font-family: -apple-system, 'Segoe UI', 'Hiragino Kaku Gothic ProN', sans-serif;
        line-height: 1.7;
        color: #222;
        max-width: 720px;
        margin: 0 auto;
        padding: 16px;
      }}
      .greeting {{
        background-color: #f1f8f1;
        border-left: 4px solid #4caf50;
        border-radius: 4px;
        padding: 12px 16px;
        margin-bottom: 24px;
      }}
      .content h1 {{
        color: #2e7d32;
        border-bottom: 3px solid #4caf50;
        padding-bottom: 8px;
      }}
      .content h2 {{
        color: #2e7d32;
        border-bottom: 1px solid #a5d6a7;
        padding-bottom: 6px;
        margin-top: 28px;
      }}
      .content h3 {{ color: #388e3c; margin-top: 20px; }}
      .content h4 {{ color: #43a047; }}
      .content hr {{ border: none; border-top: 2px solid #c8e6c9; margin: 24px 0; }}
      .content table {{ border-collapse: collapse; width: 100%; margin: 12px 0; }}
      .content th {{ background-color: #4caf50; color: #fff; padding: 8px; text-align: left; }}
      .content td {{ padding: 8px; border: 1px solid #c8e6c9; }}
      .content tr:nth-child(even) {{ background-color: #f1f8f1; }}
      .content strong {{ color: #2e7d32; }}
      .content a {{ color: #2e7d32; }}
    </style>
  </head>
  <body>
    {greeting_block}
    <div class="content">{content_html}</div>
  </body>
</html>
"""

    msg.attach(MIMEText(body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, to_addr, msg.as_string())
        print(f"[OK] メール送信完了 → {to_addr}")
        return True
    except Exception as e:
        print(f"[エラー] メール送信失敗: {e}")
        return False


# ── メイン処理 ───────────────────────────────────────────────────

def send_error_email(subject: str, error_msg: str, hint: str = ""):
    """エラー発生時に通知メールを送る（挨拶文なし・赤系ボックスで警告表示）"""
    hint_section = f"\n\n**対処方法:**\n{hint}" if hint else ""
    body = f"## エラーが発生しました\n\n{error_msg}{hint_section}"
    send_email(subject, body)


def run_check(notify: bool = True):
    # 1. リリースログ取得
    try:
        content = fetch_release_log()
    except (FileNotFoundError, RuntimeError) as e:
        print(f"[エラー] {e}")
        if notify:
            send_error_email(
                subject=f"【Optilogicエラー】セッション切れ {datetime.now().strftime('%Y/%m/%d')}",
                error_msg=str(e),
                hint=(
                    "以下のコマンドを実行してOptilogicに再ログインしてください。\n\n"
                    "```\n"
                    "cd c:\\products\\My_CosmicFrog\\release-notifier\n"
                    ".venv\\Scripts\\python.exe notifier.py --setup\n"
                    "```"
                ),
            )
        return
    except Exception as e:
        print(f"[予期せぬエラー] {e}")
        if notify:
            send_error_email(
                subject=f"【Optilogicエラー】予期せぬエラー {datetime.now().strftime('%Y/%m/%d')}",
                error_msg=str(e),
            )
        return

    # 2. 変更検知
    current_hash = get_content_hash(content)
    last_hash = load_last_hash()

    if current_hash == last_hash:
        print("[情報] 前回から変更なし。通知をスキップします。")
        return

    print("[新着] リリースログが更新されています！翻訳中...")

    # 3. Claude で翻訳（数十秒〜数分かかる場合があります）
    try:
        translated = translate_with_claude(content)
    except Exception as e:
        print(f"[翻訳エラー] {e}")
        if notify:
            send_error_email(
                subject=f"【Optilogicエラー】翻訳失敗 {datetime.now().strftime('%Y/%m/%d')}",
                error_msg=str(e),
                hint="Anthropic APIキーや残高を確認してください（console.anthropic.com）。",
            )
        return

    print("\n" + "=" * 60)
    print(translated)
    print("=" * 60 + "\n")

    # 4. ログ保存
    save_log(content, translated)

    # 5. メール通知
    if notify:
        subject = f"【Optilogic更新情報】{datetime.now().strftime('%Y/%m/%d')}"
        body = f"{EMAIL_GREETING}\n\n---\n\n{translated}"
        send_email(subject, body)

    # 6. ハッシュ更新（通知後に保存）
    save_current_hash(current_hash)


def main():
    args = sys.argv[1:]

    if "--setup" in args:
        setup_session()
    elif "--check" in args:
        run_check(notify=False)
    else:
        run_check(notify=True)


if __name__ == "__main__":
    main()
