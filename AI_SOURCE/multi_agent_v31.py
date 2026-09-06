import json, os

BASE = os.path.expanduser("~/LyTuongSong_AI")

def read(name):
    try:
        with open(os.path.join(BASE, name), encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def brain():
    return {
        "memory": read("memory.json"),
        "goals": read("goals.json"),
        "plans": read("plans.json")
    }

def research(b):
    return "🔎 Research: Phân tích thông tin và bối cảnh dự án."

def planning(b):
    for p in b["plans"]:
        if not p.get("done"):
            return "📋 Planner: " + p["step"]
    return "📋 Planner: Chưa có bước kế tiếp."

def tool(action):
    return "🛠️ Tool Agent: " + action

print("=" * 60)
print("🤖 MULTI-AGENT LÝ TƯỞNG SỐNG v3.1")
print("=" * 60)

b = brain()

print("\n👑 MANAGER AGENT")
print("→ Đang điều phối...")

print("\n" + research(b))
print(planning(b))

action = planning(b).replace("📋 Planner: ", "")

print("\n🛡️ APPROVAL")
print("→ Hành động:", action)

answer = input("👤 Duyệt? (y/n): ").strip().lower()

if answer == "y":
    print("\n" + tool(action))
    print("✅ Multi-Agent hoàn thành vòng.")
else:
    print("\n🛑 Manager dừng hành động.")

print("\n🏁 v3.1 READY")
