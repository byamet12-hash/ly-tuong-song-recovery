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

def get_action():
    plans = read("plans.json")
    pending = [p for p in plans if not p.get("done")]

    if pending:
        return pending[0]["step"]

    return "Xây bước tiếp theo cho AI Agent"

print("=" * 50)
print("🤖 AGENT LOOP v1.8")
print("=" * 50)

action = get_action()

print("\n⚙️ Agent đề xuất:")
print("→", action)

answer = input("\n🛡️ Bạn có duyệt hành động này? (y/n): ").strip().lower()

if answer == "y":
    print("\n✅ Đã duyệt.")
    print("🛠️ Thực thi:", action)
    print("💾 Agent đã hoàn thành vòng hành động.")
else:
    print("\n🛑 Agent dừng lại.")
