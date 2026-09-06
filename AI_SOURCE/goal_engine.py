import json, os

FILE = "goals.json"

def load():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

goals = load()

print("=" * 50)
print("🎯 GOAL ENGINE v2.2")
print("=" * 50)

if not goals:
    print("⚠️ Chưa có mục tiêu.")
else:
    for i, g in enumerate(goals, 1):
        print(f"{i}. {g['name']} — {g['progress']}%")

print("\n✅ Goal Engine đã sẵn sàng.")
print("💾 Dữ liệu:", FILE)
