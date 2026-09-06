import json, os

def read(f):
    if not os.path.exists(f):
        return []
    try:
        with open(f, encoding="utf-8") as x:
            return json.load(x)
    except:
        return []

while True:
    c = input("🛠️ Tool: ").strip().lower()

    if c == "thoat":
        print("👋 Đóng Tools.")
        break

    if c == "memory":
        print("💾 MEMORY:")
        for x in read("memory.json"):
            print("-", x)

    elif c == "goal":
        print("🎯 GOALS:")
        for x in read("goals.json"):
            print("-", x["name"], f"({x['progress']}%)")

    elif c == "plan":
        print("📋 PLANS:")
        for i, x in enumerate(read("plans.json"), 1):
            print(i, "✅" if x["done"] else "⏳", x["step"])

    elif c == "status":
        goals = read("goals.json")
        plans = read("plans.json")
        done = sum(x["done"] for x in plans)
        print("📊 STATUS")
        print("🎯 Goals:", len(goals))
        print("📋 Plans:", len(plans))
        print("✅ Done:", done)

    else:
        print("Dùng: memory | goal | plan | status | thoat")
