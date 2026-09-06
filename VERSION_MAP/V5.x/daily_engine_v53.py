import json, os
from datetime import date

BASE = os.path.expanduser("~/LyTuongSong_AI")
FILE = os.path.join(BASE, "daily_tasks.json")

def load(file):
    try:
        with open(os.path.join(BASE,file),encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save(file,data):
    with open(os.path.join(BASE,file),"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

tasks = load("tasks.json")
daily = load("daily_tasks.json")

today = str(date.today())

today_tasks = [x for x in daily if x.get("date") == today]

if not today_tasks:
    pending = [x for x in tasks if not x.get("done")]

    for task in pending[:3]:
        today_tasks.append({
            "date": today,
            "name": task["name"],
            "done": False
        })

    daily = [x for x in daily if x.get("date") != today]
    daily.extend(today_tasks)
    save("daily_tasks.json",daily)

print("=" * 55)
print("📅 DAILY ENGINE v5.3")
print("=" * 55)
print("📆 Hôm nay:", today)

if not today_tasks:
    print("🎉 Không còn Task hôm nay.")
else:
    for i,t in enumerate(today_tasks,1):
        status = "✅" if t["done"] else "⏳"
        print(f"{i}. {status} {t['name']}")

print("\n🎯 Ưu tiên: hoàn thành Task số 1 trước.")
print("✅ DAILY ENGINE READY")
