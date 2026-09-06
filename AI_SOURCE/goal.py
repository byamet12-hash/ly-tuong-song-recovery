import json
import os

GOAL_FILE = "goals.json"

def load_goals():
    if not os.path.exists(GOAL_FILE):
        return []
    try:
        with open(GOAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_goals(goals):
    with open(GOAL_FILE, "w", encoding="utf-8") as f:
        json.dump(goals, f, ensure_ascii=False, indent=2)

def show_goals():
    goals = load_goals()

    if not goals:
        print("🎯 Chưa có mục tiêu.")
        return

    print("\n🎯 MỤC TIÊU:")
    for i, goal in enumerate(goals, 1):
        print(f"{i}. {goal['name']} — {goal['progress']}%")
    print()

print("=" * 50)
print("🎯 GOAL AGENT LÝ TƯỞNG SỐNG v0.5")
print("=" * 50)
print("Lệnh:")
print("  mục tiêu: nội dung")
print("  tiến độ: số")
print("  xem")
print("  thoat\n")

while True:
    command = input("🎯 Goal: ").strip()

    if command.lower() == "thoat":
        print("👋 Đóng Goal Agent.")
        break

    elif command.lower() == "xem":
        show_goals()

    elif command.lower().startswith("mục tiêu:"):
        name = command[len("mục tiêu:"):].strip()

        if name:
            goals = load_goals()
            goals.append({
                "name": name,
                "progress": 0
            })
            save_goals(goals)
            print("✅ Đã tạo mục tiêu.\n")

    elif command.lower().startswith("tiến độ:"):
        try:
            progress = int(command[len("tiến độ:"):].strip())
            goals = load_goals()

            if goals:
                goals[-1]["progress"] = max(0, min(100, progress))
                save_goals(goals)
                print(f"📈 Đã cập nhật: {progress}%\n")
            else:
                print("⚠️ Chưa có mục tiêu.\n")

        except ValueError:
            print("⚠️ Hãy nhập số từ 0 đến 100.\n")

    else:
        print("Dùng: mục tiêu: ... | tiến độ: ... | xem | thoat")
