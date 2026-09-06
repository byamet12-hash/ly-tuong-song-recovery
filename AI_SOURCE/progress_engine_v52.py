import json, os

BASE = os.path.expanduser("~/LyTuongSong_AI")

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
goals = load("goals.json")

total = len(tasks)
done = sum(1 for t in tasks if t.get("done"))

progress = round(done / total * 100) if total else 0

print("=" * 55)
print("📊 PROGRESS ENGINE v5.2")
print("=" * 55)
print(f"📝 Tasks: {total}")
print(f"✅ Done:  {done}")
print(f"⏳ Todo:  {total-done}")
print(f"📈 Tiến độ thực: {progress}%")

if goals:
    goals[0]["progress"] = progress
    save("goals.json",goals)
    print(f"\n🎯 Goal → {goals[0]['progress']}%")

print("\n✅ PROGRESS ENGINE READY")
