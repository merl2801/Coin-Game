import yaml


with open(".github/ISSUE_TEMPLATE/data.yml", "r") as f:
    data = yaml.safe_load(f)


numbers = data["numbers"]
total = sum(numbers)
print(f"Tổng là: {total}")
