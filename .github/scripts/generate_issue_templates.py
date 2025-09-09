from pathlib import Path

def main():
    templatedir = Path(".github/ISSUE_TEMPLATE")

    if not templatedir.exists():
        print("❌ Không tìm thấy thư mục .github/ISSUE_TEMPLATE")
        return

    templates = (
        list(templatedir.glob("*.yml")) +
        list(templatedir.glob("*.md"))
    )

    if not templates:
        print("⚠️ Không tìm thấy file template nào trong .github/ISSUE_TEMPLATE")
        return

    print("📄 Các issue template hiện có:")
    for file in templates:
        print(f"   - {file.name}")

    print("✅ Sẵn sàng để GitHub sử dụng tất cả các template này khi tạo issue.")

if __name__ == "__main__":
    main()
