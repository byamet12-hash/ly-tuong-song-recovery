import json
import os

PLAN_FILE = "plans.json"

def load_plans():
    if not os.path.exists(PLAN_FILE):
        return []
    try:
        with open(PLAN_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_plans(plans):
    with open(PLAN_FILE, "w", encoding="utf-8") as f:
        json.dump(plans, f, ensure_ascii=False, indent=2)

def show_plans():
    plans = load_plans()

    if not plans:
        print("📋 Chưa có kế hoạch.")
        return

    print("\n📋 KẾ HOẠCH:")
    for i, plan in enumerate(plans, 1):
        status = "✅" if plan["done"] else "⏳"
        print(f"{i}. {status} {plan['step']}")
    print()

print("=" * 50)
print("📋 PLANNING AGENT LÝ TƯỞNG SỐNG v0.6")
print("=" * 50)
print("Lệnh:")
print("  bước: nội dung")
print("  xong: số")
print("  xem")
print("  thoat\n")

while True:
    command = input("📋 Plan: ").strip()

    if command.lower() == "thoat":
        print("👋 Đóng Planning Agent.")
        break

    elif command.lower() == "xem":
        show_plans()

    elif command.lower().startswith("bước:"):
        step = command[len("bước:"):].strip()

        if step:
            plans = load_plans()
            plans.append({
                "step": step,
                "done": False
            })
            save_plans(plans)
            print("✅ Đã thêm bước.\n")

    elif command.lower().startswith("xong:"):
        try:
            number = int(command[len("xong:"):].strip())
            plans = load_plans()

            if 1 <= number <= len(plans):
                plans[number - 1]["done"] = True
                save_plans(plans)
                print("🎉 Đã hoàn thành bước.\n")
            else:
                print("⚠️ Không có bước này.\n")

        except ValueError:
            print("⚠️ Hãy nhập số bước.\n")

    else:
        print("Dùng: bước: ... | xong: số | xem | thoat")
