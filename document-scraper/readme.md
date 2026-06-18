# Optilogic ドキュメントスクレイパー

Optilogic のヘルプセンター（optilogic.com/resources/help-center）を自動取得し、
Claude Project または NotebookLM に読み込ませる MD ファイルを生成するツール。

**対象ツール:** CosmicFrog / DataStar / Ada (Agentic AI) / Composable Apps

## セットアップ

[uv](https://docs.astral.sh/uv/) が必要です（初回のみ）。

```powershell
# uv のインストール（未インストールの場合）
winget install astral-sh.uv
```

依存ライブラリのインストールは不要です。`uv run` が自動で解決します。

## 実行方法

```powershell
cd c:\products\My_CosmicFrog\document-scraper

# フル実行（URL取得 → コンテンツ取得 → notebook_source.md 生成）
uv run scraper.py

# URL取得のみ（all_urls.txt を更新したいとき）
uv run scraper.py --urls

# コンテンツ取得のみ（all_urls.txt が既にある場合）
uv run scraper.py --fetch
```

認証不要: Optilogic のヘルプセンターは公開サイトのため Cookie は不要です。

## ファイル構成

| ファイル | 説明 |
|---|---|
| `scraper.py` | メインスクリプト |
| `all_urls.txt` | 取得した URL リスト（自動生成） |
| `notebook_source.md` | Claude Project / NotebookLM アップロード用 MD（自動生成） |
| `system_prompt.md` | Claude Project 用システムプロンプト |

## アシスタントの作成手順

### Claude Project を使う場合（推奨）

1. `uv run scraper.py` を実行して `notebook_source.md` を生成
2. [claude.ai](https://claude.ai) で新規 Project を作成
3. Project の「Add content」から `notebook_source.md` をアップロード
4. Project instructions に `system_prompt.md` の内容を貼り付け
5. 完了。Project 内で質問するとドキュメントに基づいた回答が得られます

### NotebookLM を使う場合

1. `uv run scraper.py` を実行して `notebook_source.md` を生成
2. [notebooklm.google.com](https://notebooklm.google.com) で新規ノートブックを作成
3. 「ソースを追加」から `notebook_source.md` をアップロード
4. 完了。チャット欄で質問できます

## ドキュメント更新時の再取得

Optilogic がドキュメントを更新した際は、以下を実行してください。

```powershell
cd c:\products\My_CosmicFrog\document-scraper
uv run scraper.py
```

再生成した `notebook_source.md` を Claude Project / NotebookLM に再アップロードしてください。

## 週次自動実行（タスクスケジューラ）

毎週月曜 9:00 に自動実行する場合（管理者 PowerShell で実行）:

```powershell
$action = New-ScheduledTaskAction -Execute "uv" -Argument "run scraper.py" -WorkingDirectory "c:\products\My_CosmicFrog\document-scraper"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At "9:00AM"
Register-ScheduledTask -TaskName "OptilogicDocScraper" -Action $action -Trigger $trigger -RunLevel Highest
```

確認・手動実行:

```powershell
schtasks /query /tn "OptilogicDocScraper" /fo LIST
schtasks /run /tn "OptilogicDocScraper"
```
