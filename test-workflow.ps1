# Test GitHub Actions Workflow
# Script để test tự động add Issues vào GitHub Project

Write-Host "Testing GitHub Actions workflow cho Project automation..." -ForegroundColor Green

# Kiểm tra workflow files
$workflowFiles = @(
    ".github/workflows/add-to-project.yml",
    ".github/workflows/auto-worklog.yml"
)

foreach ($file in $workflowFiles) {
    if (Test-Path $file) {
        Write-Host "✅ Found: $file" -ForegroundColor Green
    } else {
        Write-Host "❌ Missing: $file" -ForegroundColor Red
    }
}

# Kiểm tra Issue template
if (Test-Path ".github/ISSUE_TEMPLATE/work-item.md") {
    Write-Host "✅ Work item template ready" -ForegroundColor Green
} else {
    Write-Host "❌ Missing work item template" -ForegroundColor Red
}

Write-Host "`n🔧 Để test workflow:" -ForegroundColor Yellow
Write-Host "1. Commit và push các workflow files"
Write-Host "2. Tạo Issue mới từ template 'Work Item'"
Write-Host "3. Issue sẽ tự động được add vào Project"
Write-Host "4. Field 'Work type' sẽ được set dựa trên labels"

Write-Host "`n📋 Required setup:" -ForegroundColor Cyan
Write-Host "- PROJECT_TOKEN secret cần được config trong GitHub repository settings"
Write-Host "- Project URL đã được set đúng: https://github.com/users/merl2801/projects/8"
