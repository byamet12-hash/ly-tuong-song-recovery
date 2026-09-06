import json, os

BASE = os.path.expanduser("~/LyTuongSong_AI")
FILE = os.path.join(BASE, "tasks.json")

def read():
    try:
        with open(FILE, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

plans = []
try:
    with open(os.path.join(BASE, "plans.json"), encoding="utf-8") as f:
        plans = json.load(f)
except:
    pass

tasks = read()

for plan in plans:
    if not plan.get("done"):
        step = plan["step"]

        defaults = {
            "Xây AI Local": [
                "Kiểm tra llama.cpp",
                "Kiểm tra model Local",
                "Test Qwen Local"
            ],
            "Xây Memory": [
                "Kiểm tra memory.json",
                "Test ghi Memory",
                "Test đọc Memory"
            ],
            "Xây Goal": [
                "Kiểm tra goals.json",
                "Test cập nhật tiến độ",
                "Kết nối Goal với Plan"
            ],
            "Xây Multi-Agent": [
                "Tạo Manager Agent",
                "Tạo Research Agent",
                "Tạo Planner Agent",
                "Kết nối các Agent"
            ]
        }

        for name in defaults.get(step, [f"Phân rã: {step}"]):
            if not any(t["name"] == name for t in tasks):
                tasks.append({
                    "name": name,
                    "plan": step,
                    "done": False
                })

save(tasks)

print("=" * 55)
print("📝 TASK ENGINE v5.1")
print("=" * 55)

for i, t in enumerate(tasks, 1):
    status = "✅" if t["done"] else "⏳"
    print(f"{i}. {status} {t['name']}")

print("\n✅ TASK ENGINE READY")
print("💾 Đã lưu:", FILE)
