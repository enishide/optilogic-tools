# Optilogic リリースログ 通知スクリプト

`https://optilogic.app/#/release-log` を定期チェックし、更新があれば日本語に翻訳してメールで通知します。

## セットアップ（初回のみ）

### 1. uv のインストール（未インストールの場合）

```powershell
winget install astral-sh.uv
```

### 2. Playwright のブラウザをインストール

```powershell
cd c:\products\My_CosmicFrog\release-notifier
uv run playwright install chromium
```

### 3. .env ファイルを作成してメール設定を記入

```powershell
Copy-Item .env.example .env
notepad .env
```

**Gmail アプリパスワードの取得方法:**
1. Googleアカウント（myaccount.google.com）を開く
2. **セキュリティ** → **2段階認証プロセス** を有効化
3. **アプリパスワード** → 「その他」→ `OptilogicNotifier` と入力 → 生成
4. 生成された16桁のパスワードを `.env` の `SMTP_PASS` に貼り付け

### 4. ブラウザログイン（セッション保存）

```powershell
cd c:\products\My_CosmicFrog\release-notifier
uv run notifier.py --setup
```

ブラウザが開くので Optilogic にログインし、リリースログページが表示されたらターミナルに戻って Enter を押します。

## 実行方法

```powershell
# 通常実行（変更があればメール通知）
uv run notifier.py

# 通知なしで内容確認のみ
uv run notifier.py --check
```

## ファイル構成

| ファイル | 説明 |
|---|---|
| `notifier.py` | メインスクリプト |
| `.env` | メール設定（要作成） |
| `.env.example` | 設定テンプレート |
| `session.json` | ブラウザセッション（自動生成） |
| `last_hash.txt` | 前回取得内容のハッシュ（変更検知用） |
| `logs/` | 翻訳結果のログ（日付付きMDファイル） |

## 週次自動実行（タスクスケジューラ）

タスク `OptilogicReleaseNotifier` が毎週月曜 9:05 に自動実行されます。

```powershell
# 手動で今すぐ実行
schtasks /run /tn "OptilogicReleaseNotifier"

# タスクの確認
schtasks /query /tn "OptilogicReleaseNotifier" /fo LIST
```

## セッション切れの対処

`session.json` は定期的に失効します（通常数日〜数週間）。
失効した場合はタスクのログに「セッションが期限切れ」と記録されます。

```powershell
uv run notifier.py --setup
```

を再実行してセッションを更新してください。

## 動作の仕組み

1. **Playwright**（ヘッドレスブラウザ）でログイン済みセッションを使い、リリースログページを取得
2. 前回取得内容のハッシュと比較 → 変更がなければ何もしない
3. 変更があれば **Claude API** で日本語翻訳
4. **Gmail SMTP** でメール送信
5. `logs/` フォルダに翻訳結果を保存
