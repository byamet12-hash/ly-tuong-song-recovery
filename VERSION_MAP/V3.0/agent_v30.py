import json, os
from datetime import datetime

BASE = os.path.expanduser("~/LyTuongSong_AI")

def read(name):
    try:
        with open(os.path.join(BASE, name), encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def write(name, data):
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def brain():
    return {
        "memory": read("memory.json"),
        "goals": read("goals.json"),
        "plans": read("plans.json")
    }

def show_brain(b):
    print("\n🧠 PROJECT BRAIN")
    print("💾 Memory:", len(b["memory"]))
    print("🎯 Goals:", len(b["goals"]))
    print("📋 Plans:", len(b["plans"]))

    for g in b["goals"]:
        print(f"  🎯 {g['name']} — {g['progress']}%")

    for p in b["plans"]:
        print(f"  {'✅' if p.get('done') else '⏳'} {p['step']}")

def next_action(b):
    for p in b["plans"]:
        if not p.get("done"):
            return p["step"]
    return "Xây bước tiếp theo cho AI Agent"

def save_result(text):
    memory = read("memory.json")
    memory.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "content": text
    })
    write("memory.json", memory)

print("=" * 60)
print("🤖 AI AGENT LÝ TƯỞNG SỐNG v3.0")
print("🧠 Brain + ⚙️ Action + 🛡️ Approval + 🛠️ Executor")
print("=" * 60)

b = brain()
show_brain(b)

action = next_action(b)

print("\n⚙️ ACTION ĐỀ XUẤT")
print("→", action)

answer = input("\n🛡️ Duyệt hành động? (y/n): ").strip().lower()

if answer == "y":
    print("\n🛠️ EXECUTOR")
    print("→ Thực thi:", action)

    result = f"Đã duyệt và thực thi: {action}"
    save_result(result)

    print("✅ Thành công.")
    print("💾 Kết quả đã ghi vào Memory.")
else:
    print("\n🛑 Agent dừng.")
