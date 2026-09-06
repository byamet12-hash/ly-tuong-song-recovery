import json, os
from datetime import datetime, date

BASE=os.path.expanduser("~/LyTuongSong_AI")

def load(f):
    try:
        with open(os.path.join(BASE,f),encoding="utf-8") as x:
            return json.load(x)
    except:
        return []

def save(f,d):
    with open(os.path.join(BASE,f),"w",encoding="utf-8") as x:
        json.dump(d,x,ensure_ascii=False,indent=2)

def brain():
    return {
        "memory":load("memory.json"),
        "goals":load("goals.json"),
        "plans":load("plans.json"),
        "tasks":load("tasks.json"),
        "daily":load("daily_tasks.json")
    }

def progress(b):
    total=len(b["tasks"])
    done=sum(x.get("done",False) for x in b["tasks"])
    return round(done/total*100) if total else 0

def next_task(b):
    for x in b["tasks"]:
        if not x.get("done"):
            return x["name"]
    return None

def remember(text):
    d=load("memory.json")
    d.append({
        "time":datetime.now().isoformat(timespec="seconds"),
        "content":text
    })
    save("memory.json",d)

def dashboard():
    b=brain()
    p=progress(b)
    print("\n🧠 PROJECT BRAIN v6.0")
    print("💾 Memory:",len(b["memory"]))
    print("🎯 Goals:",len(b["goals"]))
    print("📋 Plans:",len(b["plans"]))
    print("📝 Tasks:",len(b["tasks"]))
    print("📊 Progress:",str(p)+"%")

def agent():
    b=brain()
    task=next_task(b)

    if not task:
        print("🎉 Không còn Task chưa hoàn thành.")
        return

    print("\n👑 MANAGER")
    print("🎯 Goal:",b["goals"][0]["name"] if b["goals"] else "Chưa có")
    print("⚙️ Đề xuất:",task)

    ok=input("🛡️ Duyệt? (y/n): ").strip().lower()

    if ok!="y":
        print("🛑 Dừng.")
        return

    print("🛠️ EXECUTOR →",task)

    for x in b["tasks"]:
        if x["name"]==task:
            x["done"]=True

    save("tasks.json",b["tasks"])

    p=progress(brain())

    goals=load("goals.json")
    if goals:
        goals[0]["progress"]=p
        save("goals.json",goals)

    remember(f"Hoàn thành Task: {task}. Tiến độ: {p}%")

    print("✅ Task hoàn thành.")
    print("📊 Progress:",p,"%")
    print("💾 Memory đã cập nhật.")

print("="*60)
print("🤖 AI AGENT LÝ TƯỞNG SỐNG v6.0")
print("🏭 AUTONOMOUS PROJECT ENGINE")
print("="*60)

dashboard()

while True:
    q=input("\n👤 Bạn: ").strip

