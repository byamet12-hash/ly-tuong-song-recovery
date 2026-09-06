import json, os

def read(f):
    if not os.path.exists(f):
        return []
    try:
        with open(f, encoding="utf-8") as x:
            return json.load(x)
    except:
        return []

def suggest():
    goals = read("goals.json")
    plans = read("plans.json")

    print("\n⚙️ ACTION ENGINE v1.5")

    if goals:
        print("🎯 Mục tiêu:")
        for g in goals:
            print(f"- {g['name']} ({g['progress']}%)")

    pending = [p for p in plans if not p.get("done")]

    if pending:
        print("\n📋 Hành động đề xuất:")
        print("→", pending[0]["step"])
    else:
        print("\n📋 Chưa có bước kế tiếp.")

suggest()
