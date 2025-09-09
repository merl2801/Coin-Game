import sys

feature = int(sys.argv[1])
bug = int(sys.argv[2])
ot = int(sys.argv[3])

kpi = (feature * 10) - (bug * 5) - (ot * 2)

if kpi >= 80:
    rating = "🌟 Tốt"
elif kpi >= 50:
    rating = "⚖️ Trung bình"
else:
    rating = "❗ Kém"

print(f"{kpi}|{rating}")
