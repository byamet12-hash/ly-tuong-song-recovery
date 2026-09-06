import json, os, subprocess
from datetime import datetime

BASE = os.path.expanduser("~/LyTuongSong_AI")

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
        "memory": read("memory.json")[-5:],
        "goals": read("goals.json"),
        "plans": read("plans.json")
    }

def next_action():
    for p in read("plans.json"):
        if not p.get("done"):
            return p.get("step")
    return "Xây bước tiếp theo cho AI Agent"

def remember(text):
    data=read("memory.json")
    data.append({
        "time":datetime.now().isoformat(timespec="seconds"),
        "content":text
    })
    save("memory.json",data)

def qwen(question):
    llama=os.path.join(BASE,"llama.cpp/build/bin/llama-cli")
    models=os.path.join(BASE,"models")

    if not os.path.exists(llama):
        return "⚠️ Chưa tìm thấy llama-cli."

    gguf=[
        os.path.join(models,x)
        for x in os.listdir(models)
        if x.endswith(".gguf")
    ] if os.path.isdir(models) else []

    if not gguf:
        return "⚠️ Chưa có model GGUF trong models/."

    b=brain()

    prompt=f"""Bạn là AI Lý Tưởng Sống.
Trả lời bằng tiếng Việt, ngắn gọn và hữu ích.
Hãy sử dụng bối cảnh dự án bên dưới.

MEMORY:
{b["memory"]}

GOALS:
{b["goals"]}

PLANS:
{b["plans"]}

CÂU HỎI:
{question}
"""

    try:
        r=subprocess.run(
            [llama,"-m",gguf[0],"-c","2048","-n","250","-p",prompt],
            capture_output=True,text=True,timeout=120
        )
        return r.stdout.strip()
    except Exception as e:
        return "⚠️ Qwen Local lỗi: "+str(e)

def agent():
    b=brain()
    action=next_action()

    print("\n🧠 PROJECT BRAIN")
    print("💾 Memory:",len(b["memory"]))
    print("🎯 Goals:",len(b["goals"]))
    print("📋 Plans:",len(b["plans"]))

    print("\n👑 MANAGER")
    print("⚙️ Hành động đề xuất:",action)

    ok=input("🛡️ Duyệt? (y/n): ").strip().lower()

    if ok=="y":
        print("\n🛠️ EXECUTOR →",action)
        remember("Đã duyệt: "+action)
        print("💾 Đã ghi kết quả vào Memory.")
        print("✅ Agent v4.0 hoàn tất vòng.")
    else:
        print("🛑 Agent dừng.")

print("="*60)
print("🤖 AI AGENT LÝ TƯỞNG SỐNG v4.0")
print("🧠 Qwen Local + Project Brain + Agent")
print("="*60)
print("Lệnh: brain | action | agent | ai: nội dung | remember: nội dung | thoat")

while True:
    q=input("\n👤 Bạn: ").strip()

    if q.lower()=="thoat":
        print("👋 Đóng Agent.")
        break

    elif q.lower()=="brain":
        b=brain()
        print("\n🧠 BRAIN")
        print("💾 Memory:",len(b["memory"]))
        print("🎯 Goals:",b["goals"])
        print("📋 Plans:",b["plans"])

    elif q.lower()=="action":
        print("\n⚙️ ACTION →",next_action())

    elif q.lower()=="agent":
        agent()

    elif q.lower().startswith("ai:"):
        print("\n🤖 QWEN LOCAL")
        print(qwen(q[3:].strip()))

    elif q.lower().startswith("remember:"):
        remember(q[9:].strip())
        print("💾 Đã lưu Memory.")

    else:
        print("Dùng: brain | action | agent | ai: nội dung | remember: nội dung | thoat")
