import json, os
from datetime import datetime

BASE=os.path.expanduser("~/LyTuongSong_AI")

def read(f):
    try:
        with open(os.path.join(BASE,f),encoding="utf-8") as x:
            return json.load(x)
    except:
        return []

def save(f,data):
    with open(os.path.join(BASE,f),"w",encoding="utf-8") as x:
        json.dump(data,x,ensure_ascii=False,indent=2)

def brain():
    return {
        "memory":read("memory.json")[-5:],
        "goals":read("goals.json"),
        "plans":read("plans.json")
    }

def add_plan(step):
    plans=read("plans.json")
    if not any(p.get("step")==step for p in plans):
        plans.append({"step":step,"done":False})
        save("plans.json",plans)
        return True
    return False

def next_action():
    for p in read("plans.json"):
        if not p.get("done"):
            return p.get("step")
    return None

def remember(text):
    data=read("memory.json")
    data.append({
        "time":datetime.now().isoformat(timespec="seconds"),
        "content":text
    })
    save("memory.json",data)

def plan_from_goal():
    goals=read("goals.json")
    if not goals:
        return

    goal=goals[0]["name"]

    suggestions=[
        "Xây AI Local",
        "Xây Memory",
        "Xây Goal",
        "Xây Multi-Agent"
    ]

    print("\n🧠 GOAL ENGINE")
    print("🎯 Mục tiêu:",goal)
    print("\n📋 KẾ HOẠCH ĐỀ XUẤT:")

    for s in suggestions:
        print("→",s)

    ok=input("\n🛡️ Thêm các bước này vào Plan? (y/n): ").strip().lower()

    if ok=="y":
        for s in suggestions:
            add_plan(s)
        print("✅ Đã cập nhật Plan.")
    else:
        print("🛑 Không thay đổi Plan.")

print("="*60)
print("🤖 AI AGENT LÝ TƯỞNG SỐNG v5.0")
print("🎯 GOAL → 📋 PLAN → ⚙️ ACTION")
print("="*60)

b=brain()

print("\n🎯 GOALS")
for g in b["goals"]:
    print(f"• {g['name']} — {g['progress']}%")

plan_from_goal()

print("\n⚙️ ACTION TIẾP THEO")
a=next_action()

if a:
    print("→",a)
else:
    print("→ Chưa có hành động.")

print("\n🏁 v5.0 READY")
