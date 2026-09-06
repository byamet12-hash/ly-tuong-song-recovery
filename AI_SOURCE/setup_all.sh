#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "🏭 LÝ TƯỞNG SỐNG AI — FULL SETUP"

mkdir -p config models

[ -f memory.json ] || echo '[]' > memory.json
[ -f goals.json ] || printf '[{"name":"Xây hệ sinh thái AI Agent Lý Tưởng Sống","progress":10}]' > goals.json
[ -f plans.json ] || printf '[{"step":"Xây AI Local","done":false},{"step":"Xây Memory","done":false},{"step":"Xây Goal","done":false},{"step":"Xây Multi-Agent","done":false}]' > plans.json

cat > lytuongsong.py <<'PY'
import json, os, subprocess
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
        "memory":read("memory.json"),
        "goals":read("goals.json"),
        "plans":read("plans.json")
    }

def show():
    b=brain()
    print("\n🧠 PROJECT BRAIN")
    print("💾 MEMORY:",len(b["memory"]))
    for x in b["memory"][-5:]:
        print("  └─",x.get("content",x) if isinstance(x,dict) else x)

    print("\n🎯 GOALS")
    for x in b["goals"]:
        print(f"  └─ {x.get('name')} ({x.get('progress',0)}%)")

    print("\n📋 PLANS")
    for x in b["plans"]:
        print(f"  └─ {'✅' if x.get('done') else '⏳'} {x.get('step')}")

def next_action():
    for x in read("plans.json"):
        if not x.get("done"):
            return x.get("step")
    return "Xây bước tiếp theo cho AI Agent"

def remember(text):
    data=read("memory.json")
    data.append({
        "time":datetime.now().isoformat(timespec="seconds"),
        "content":text
    })
    save("memory.json",data)

def local_ai(q):
    llama=os.path.join(BASE,"llama.cpp/build/bin/llama-cli")
    models=os.path.join(BASE,"models")

    found=[]
    if os.path.isdir(models):
        found=[os.path.join(models,x) for x in os.listdir(models)
               if x.endswith(".gguf")]

    if not os.path.exists(llama):
        return "⚠️ llama.cpp chưa sẵn sàng."
    if not found:
        return "⚠️ Chưa tìm thấy model GGUF trong models/."

    b=brain()
    prompt=f"""Bạn là AI Lý Tưởng Sống.
Trả lời tiếng Việt, ngắn gọn, hữu ích.

MEMORY:
{b["memory"][-5:]}

GOALS:
{b["goals"]}

PLANS:
{b["plans"]}

CÂU HỎI:
{q}
"""

    try:
        r=subprocess.run(
            [llama,"-m",found[0],"-c","2048","-n","200","-p",prompt],
            capture_output=True,text=True,timeout=120
        )
        return r.stdout.strip()
    except Exception as e:
        return "⚠️ Local AI lỗi: "+str(e)

def agent():
    b=brain()
    action=next_action()

    print("\n👑 MANAGER")
    print("🧠 Context:",len(b["memory"]),"Memory |",
          len(b["goals"]),"Goals |",len(b["plans"]),"Plans")

    print("🔎 RESEARCH → phân tích bối cảnh")
    print("📋 PLANNER →",action)
    print("🛠️ TOOL → sẵn sàng")

    ok=input("\n🛡️ Duyệt hành động? (y/n): ").strip().lower()

    if ok!="y":
        print("🛑 Agent dừng.")
        return

    print("🛠️ EXECUTOR →",action)
    result="Đã duyệt hành động: "+action
    remember(result)
    print("💾 MEMORY → đã lưu kết quả.")
    print("✅ VÒNG AGENT HOÀN TẤT.")

print("="*60)
print("🤖 AI AGENT LÝ TƯỞNG SỐNG — FULL SYSTEM")
print("="*60)
print("Lệnh: brain | action | agent | ai: nội dung | remember: nội dung | thoat")

while True:
    q=input("\n👤 Bạn: ").strip()

    if q.lower()=="thoat":
        print("👋 Đóng hệ thống.")
        break

    if q.lower()=="brain":
        show()
    elif q.lower()=="action":
        print("⚙️ ACTION →",next_action())
    elif q.lower()=="agent":
        agent()
    elif q.lower().startswith("ai:"):
        print("\n📱 LOCAL AI:\n",local_ai(q[3:].strip()))
    elif q.lower().startswith("remember:"):
        remember(q[9:].strip())
        print("💾 Đã lưu Memory.")
    else:
        print("Dùng: brain | action | agent | ai: nội dung | remember: nội dung | thoat")
PY

chmod +x setup_all.sh

echo ""
echo "✅ FULL SYSTEM ĐÃ SẴN SÀNG"
echo "🚀 Khởi động:"
python lytuongsong.py
