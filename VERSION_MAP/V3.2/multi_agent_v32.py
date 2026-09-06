import json, os
from datetime import datetime

BASE = os.path.expanduser("~/LyTuongSong_AI")

def read(f):
    try:
        with open(os.path.join(BASE, f), encoding="utf-8") as x:
            return json.load(x)
    except:
        return []

def write(f, data):
    with open(os.path.join(BASE, f), "w", encoding="utf-8") as x:
        json.dump(data, x, ensure_ascii=False, indent=2)

def context():
    return {
        "memory": read("memory.json")[-5:],
        "goals": read("goals.json"),
        "plans": read("plans.json")
    }

def next_action(c):
    for p in c["plans"]:
        if not p.get("done"):
            return p.get("step")
    return "Xây bước tiếp theo cho AI Agent"

def save_result(text):
    data = read("memory.json")
    data.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "content": text
    })
    write("memory.json", data)

print("=" * 60)
print("🤖 MULTI-AGENT v3.2")
print("🏭 AI AGENT LÝ TƯỞNG SỐNG")
print("=" * 60)

c = context()

print("\n🧠 CONTEXT ENGINE")
print("💾 Memory:", len(c["memory"]))
print("🎯 Goals:", len(c["goals"]))
print("📋 Plans:", len(c["plans"]))

print("\n👑 MANAGER")
print("→ Phân phối Context cho các Agent.")

print("\n🔎 RESEARCH AGENT")
print("→ Phân tích bối cảnh dự án.")

action = next_action(c)

print("\n📋 PLANNER AGENT")
print("→ Bước đề xuất:", action)

print("\n🛠️ TOOL AGENT")
print("→ Sẵn sàng thực hiện:", action)

print("\n🛡️ APPROVAL")
ok = input("👤 Duyệt hành động? (y/n): ").strip().lower()

if ok == "y":
    print("\n🛠️ EXECUTOR")
    print("→ Thực thi có kiểm soát:", action)

    result = "Multi-Agent đã hoàn thành: " + action
    save_result(result)

    print("💾 MEMORY → Đã lưu kết quả.")
    print("✅ VÒNG MULTI-AGENT HOÀN TẤT.")
else:
    print("🛑 Manager dừng toàn bộ hành động.")

print("\n🏁 MULTI-AGENT v3.2 READY")
