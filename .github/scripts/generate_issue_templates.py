from pathlib import Path

def main():
    # Thư mục chứa các issue template đã có sẵn
    templatedir = Path(".github/ISSUE_TEMPLATE")

    if not templatedir.exists():
        print("❌ Không tìm thấy thư mục .github/ISSUE_TEMPLATE")
        return

    # Liệt kê tất cả các file .yml hoặc .yaml trong thư mục đó
    templates = list(templatedir.glob("*.yml")) + list(templatedir.glob("*.yaml"))

    if not templates:
        print("⚠️ Không tìm thấy file template nào trong .github/ISSUE_TEMPLATE")
        return

    print("📄 Các issue template hiện có:")
    for file in templates:
        print(f"   - {file.name}")

    print("✅ Sẵn sàng để GitHub sử dụng tất cả các template này khi tạo issue.")

if __name__ == "__main__":
    main()
