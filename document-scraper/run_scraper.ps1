# Optilogic ドキュメントスクレイパー 実行スクリプト
# Windows タスクスケジューラから呼び出す用

$ScriptDir    = Split-Path -Parent $MyInvocation.MyCommand.Path
$NotifyScript = "$ScriptDir\..\..\notify_doc_update.py"
$UrlsFile     = "$ScriptDir\all_urls.txt"
$UrlsBackup   = "$ScriptDir\all_urls_prev.txt"
$env:PYTHONIOENCODING = "utf-8"

Set-Location $ScriptDir

# スクレイパー実行前に URL 一覧をバックアップ
if (Test-Path $UrlsFile) {
    Copy-Item $UrlsFile $UrlsBackup -Force
}

# スクレイパー実行
uv run "$ScriptDir\scraper.py"

# 変更通知（Python スクリプトが差分判定 → Gmail 送信）
if (Test-Path $UrlsBackup) {
    uv run $NotifyScript --tool "Optilogic" --old-urls $UrlsBackup --new-urls $UrlsFile
} else {
    Write-Host "[情報] 初回実行のため比較対象なし。次回から通知します。"
}
