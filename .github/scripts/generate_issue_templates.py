from pathlib import Path

# Nội dung sample cho 3 issue template
BUG_TEMPLATE = """name: 🐞 Bug report
description: Báo cáo lỗi để giúp chúng tôi cải thiện
title: "[BUG] <mô tả ngắn>"
labels: [bug]
assignees: []
body:
  - type: textarea
    id: description
    attributes:
      label: Mô tả lỗi
      description: Mô tả chi tiết về lỗi gặp phải
      placeholder: Khi tôi làm X thì Y xảy ra...
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: Các bước tái hiện
      description: Làm sao để tái hiện lỗi này?
      placeholder: |
        1. ...
        2. ...
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: Kết quả mong đợi
      description: Bạn kỳ vọng điều gì sẽ xảy ra?
      placeholder: Hệ thống sẽ ...
    validations:
      required: true
"""

FEATURE_TEMPLATE = """name: ✨ Feature request
description: Gợi ý tính năng mới hoặc cải tiến
title: "[Feature] <tên tính năng>"
labels: [enhancement]
assignees: []
body:
  - type: textarea
    id: motivation
    attributes:
      label: Động lực
      description: Tại sao tính năng này quan trọng?
      placeholder: Người dùng đang gặp khó khăn gì?
    validations:
      required: true

  - type: textarea
    id: solution
    attributes:
      label: Giải pháp gợi ý
      description: Bạn mong muốn giải pháp hoạt động thế nào?
      placeholder: Hệ thống sẽ thêm ...
    validations:
      required: true
"""

TECH_DEBT_TEMPLATE = """name: 🛠️ Tech Debt
description: Theo dõi nợ kỹ thuật trong codebase
title: "[Tech Debt] <khu vực ảnh hưởng>"
labels: [tech-debt]
assignees: []
body:
  - type: textarea
    id: context
    attributes:
      label: Ngữ cảnh
      description: Phần code nào đang gây khó khăn?
      placeholder: File/module/class nào...
    validations:
      required: true

  - type: textarea
    id: proposal
    attributes:
      label: Đề xuất cải tiến
      description: Làm sao để giảm bớt nợ kỹ thuật?
      placeholder: Refactor, thêm test, đổi lib...
"""

def main():
    outdir = Path(".github/ISSUE_TEMPLATE")
    outdir.mkdir(parents=True, exist_ok=True)

    files = {
        "bug_report.yml": BUG_TEMPLATE,
        "feature_request.yml": FEATURE_TEMPLATE,
        "tech_debt.yml": TECH_DEBT_TEMPLATE,
    }

    for fname, content in files.items():
        fpath = outdir / fname
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Generated {fpath}")

if __name__ == "__main__":
    main()
