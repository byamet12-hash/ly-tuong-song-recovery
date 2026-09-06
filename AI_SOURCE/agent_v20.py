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

def context():
    memory = read("memory.json")
    goals = read("goals.json")
    plans = read("plans.json")

    print("\n🧠 CONTEXT")
    print("💾 Memory:", len(memory))
    print("🎯 Goals:", len(goals))
    print("📋 Plans:", len(plans))

def next_action():
    plans = read("plans.json")
    for item in plans:
        if not item.get("done"):
            return item["step"]
    return "Xây bước tiếp theo cho AI Agent"

def execute(action):
    print("🛠️ EXECUTOR")
    print("→", action)
    print("✅ Đã thực thi mô phỏng.")

print("=" * 55)
print("🤖 AI AGENT LÝ TƯỞNG SỐNG v2.0")
print("=" * 55)

context()

action = next_action()

print("\n⚙️ ACTION:")
print("→", action)

answer = input("\n🛡️ Duyệt hành động? (y/n): ").strip().lower()

if answer == "y":
    execute(action)
    print("\n💾 RESULT: Thành công")
else:
    print("\n🛑 Agent dừng lại.")
