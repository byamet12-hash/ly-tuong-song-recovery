import json
import os

def read(file):
    if not os.path.exists(file):
        return []
    try:
        with open(file, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def status():
    memory = read("memory.json")
    goals = read("goals.json")
    plans = read("plans.json")

    done = sum(1 for x in plans if x.get("done"))

    print("\n🏭 CORE LÝ TƯỞNG SỐNG v1.0")
    print("🧠 AI Local:     READY")
    print("💾 Memory:", len(memory))
    print("🎯 Goals:", len(goals))
    print("📋 Plans:", len(plans))
    print("✅ Done:", done)
    print()

def route(command):
    q = command.lower()

    if any(x in q for x in ["memory", "nhớ", "ghi nhớ"]):
        return "💾 MEMORY"

    if any(x in q for x in ["goal", "mục tiêu", "tiến độ"]):
        return "🎯 GOAL"

    if any(x in q for x in ["plan", "kế hoạch", "bước"]):
        return "📋 PLANNING"

    if any(x in q for x in ["tool", "công cụ", "status"]):
        return "🛠️ TOOLS"

    return "🧠 LOCAL AI"

print("=" * 55)
print("🏭 CORE LÝ TƯỞNG SỐNG v1.0")
print("=" * 55)
print("Lệnh: status | route: nội dung | thoat\n")

while True:
    command = input("🏭 Core: ").strip()

    if command.lower() == "thoat":
        print("👋 Đóng Core.")
        break

    if command.lower() == "status":
        status()
        continue

    if command.lower().startswith("route:"):
        task = command[6:].strip()
        print("🔀 →", route(task))
        continue

    print("Dùng: status | route: nội dung | thoat")
