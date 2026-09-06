import json
import os

ALLOWED = {
    "status": "Xem trạng thái hệ thống",
    "goal": "Xem mục tiêu",
    "plan": "Xem kế hoạch",
}

def read(file):
    if not os.path.exists(file):
        return []
    try:
        with open(file, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def execute(tool):
    if tool not in ALLOWED:
        print("🛑 Tool không được phép.")
        return

    print("🛠️ EXECUTOR →", ALLOWED[tool])

    if tool == "status":
        print("📊 Memory:", len(read("memory.json")))
        print("🎯 Goals:", len(read("goals.json")))
        print("📋 Plans:", len(read("plans.json")))

    elif tool == "goal":
        for x in read("goals.json"):
            print(f"🎯 {x['name']} ({x['progress']}%)")

    elif tool == "plan":
        for x in read("plans.json"):
            print(f"{'✅' if x['done'] else '⏳'} {x['step']}")

print("🛠️ TOOL EXECUTOR v1.9")
print("Tools:", ", ".join(ALLOWED))
print("Gõ 'thoat' để đóng.\n")

while True:
    tool = input("🛠️ Tool: ").strip().lower()

    if tool == "thoat":
        print("👋 Đóng Executor.")
        break

    execute(tool)
