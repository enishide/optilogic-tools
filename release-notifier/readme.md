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

## 週次自動実行（GitHub Actions）

ワークフロー `.github/workflows/release-notifier.yml` が毎週月曜 9:00 JST に自動実行されます
（GitHub 側の遅延で実際は 11:30〜13:00 頃になることがあります）。
新着がない週はメールは送信されません。

| 用途 | URL |
|---|---|
| リポジトリ | https://github.com/enishide/optilogic-tools |
| 実行履歴・手動実行 | https://github.com/enishide/optilogic-tools/actions/workflows/release-notifier.yml |
| Secret 設定 | https://github.com/enishide/optilogic-tools/settings/secrets/actions |

手動で今すぐ実行する場合は、実行履歴ページの **Run workflow** を押します。

## メール送信先（NOTIFY_TO）の変更

送信先は GitHub の Secret `NOTIFY_TO` で管理しています。
カンマ区切りで複数指定でき、**全員 Bcc で送信**されるため宛先同士にアドレスは見えません
（To 欄には送信元 `SMTP_USER` が表示されます）。

1. 上記の **Secret 設定** ページを開く（リポジトリ所有アカウント `enishide` でログイン）
2. 「Repository secrets」の `NOTIFY_TO` の鉛筆アイコン（Update）をクリック
3. 宛先をカンマ区切りで入力し **Update secret** をクリック

```
e.nishide@bigm.one, xxx@bigm.one
```

> **注意:** Secret の値は保存後に表示できません。宛先を追加・削除するときは、
> 全員分のアドレスを入力し直してください。現在の宛先一覧は別途控えておくと安全です。

ローカルで実行する場合は `.env` の `NOTIFY_TO` も同じ形式で設定します。

## セッション切れの対処

`session.json` は定期的に失効します（通常数日〜数週間）。
失効した場合は「【Optilogicエラー】セッション切れ」の通知メールが届きます。

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
