import json, os, subprocess
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

def brain():
    return {
        "memory": read("memory.json"),
        "goals": read("goals.json"),
        "plans": read("plans.json")
    }

def show():
    b = brain()
    print("\n🧠 PROJECT BRAIN")
    print("💾 Memory:", len(b["memory"]))
    print("🎯 Goals:", len(b["goals"]))
    print("📋 Plans:", len(b["plans"]))

    for g in b["goals"]:
        print(f"🎯 {g.get('name')} — {g.get('progress',0)}%")

    for p in b["plans"]:
        print(f"{'✅' if p.get('done') else '⏳'} {p.get('step')}")

def action():
    b = brain()
    for p in b["plans"]:
        if not p.get("done"):
            return p.get("step")
    return "Xây bước tiếp theo cho AI Agent"

def memory_add(text):
    data = read("memory.json")
    data.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "content": text
    })
    write("memory.json", data)

def local_ai(q):
    model = "models/qwen2.5-1.5b-instruct-q4_k_m.gguf"
    llama = "llama.cpp/build/bin/llama-cli"

    if not os.path.exists(model) or not os.path.exists(llama):
        return "⚠️ Local AI chưa sẵn sàng."

    b = brain()
    context = (
        "Bạn là AI Lý Tưởng Sống.\n"
        "Hãy trả lời tiếng Việt, ngắn gọn và hữu ích.\n\n"
        f"MEMORY: {b['memory'][-5:]}\n"
        f"GOALS: {b['goals']}\n"
        f"PLANS: {b['plans']}\n\n"
        f"CÂU HỎI: {q}"
    )

    try:
        r = subprocess.run(
            [llama, "-m", model, "-c", "2048", "-n", "200", "-p", context],
            capture_output=True, text=True, timeout=120
        )
        return r.stdout.strip()
    except Exception as e:
        return "⚠️ Local AI lỗi: " + str(e)

def run():
    print("=" * 60)
    print("🤖 AI AGENT LÝ TƯỞNG SỐNG — ALL IN ONE")
    print("🏭 v0.x → v1.x → v2.x → v3.1")
    print("=" * 60)
    print("Lệnh: brain | action | ai: nội dung | agent | thoat")

    while True:
        q = input("\n👤 Bạn: ").strip()

        if q.lower() == "thoat":
            print("👋 Đóng Xưởng.")
            break

        if q.lower() == "brain":
            show()
            continue

        if q.lower() == "action":
            print("\n⚙️ ACTION →", action())
            continue

        if q.lower() == "agent":
            a = action()
            print("\n👑 MANAGER →", a)
            print("🔎 RESEARCH → phân tích bối cảnh")
            print("📋 PLANNER →", a)
            ok = input("🛡️ Duyệt? (y/n): ").strip().lower()

            if ok == "y":
                print("🛠️ EXECUTOR →", a)
                memory_add("Đã duyệt và thực thi: " + a)
                print("💾 RESULT → Đã ghi Memory.")
            else:
                print("🛑 Agent dừng.")
            continue

        if q.lower().startswith("ai:"):
            question = q[3:].strip()
            print("\n📱 LOCAL AI:")
            print(local_ai(question))
            continue

        print("🏭 Core: chưa có lệnh này.")
        print("Dùng: brain | action | ai: nội dung | agent | thoat")

run()
