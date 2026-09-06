import json, os

FILES = {
    "💾 MEMORY": "memory.json",
    "🎯 GOALS": "goals.json",
    "📋 PLANS": "plans.json"
}

def read(file):
    if not os.path.exists(file):
        return []
    try:
        with open(file, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

print("=" * 60)
print("🧠 PROJECT BRAIN v2.3")
print("🏭 AI AGENT LÝ TƯỞNG SỐNG")
print("=" * 60)

for title, file in FILES.items():
    data = read(file)

    print(f"\n{title}")

    if not data:
        print("  └─ Chưa có dữ liệu")
        continue

    for item in data:
        if isinstance(item, dict):
            if "name" in item:
                print(f"  └─ {item['name']} ({item.get('progress', 0)}%)")
            elif "step" in item:
                status = "✅" if item.get("done") else "⏳"
                print(f"  └─ {status} {item['step']}")
            elif "content" in item:
                print(f"  └─ {item['content']}")
        else:
            print(f"  └─ {item}")

print("\n" + "=" * 60)
print("✅ PROJECT BRAIN ĐÃ KẾT NỐI MEMORY + GOAL + PLAN")
print("=" * 60)
