import json
import os
import subprocess
import urllib.request
import urllib.error

MODEL = "models/qwen2.5-1.5b-instruct-q4_k_m.gguf"
LLAMA = "llama.cpp/build/bin/llama-cli"

def read(file):
    if not os.path.exists(file):
        return []
    try:
        with open(file, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def tool(q):
    q = q.lower()

    if "memory" in q or "trí nhớ" in q:
        return "💾 Memory:\n" + "\n".join(
            "- " + str(x) for x in read("memory.json")
        )

    if "mục tiêu" in q or "goal" in q:
        return "🎯 Goals:\n" + "\n".join(
            f"- {x['name']} ({x['progress']}%)"
            for x in read("goals.json")
        )

    if "kế hoạch" in q or "plan" in q:
        return "📋 Plans:\n" + "\n".join(
            f"- {'✅' if x['done'] else '⏳'} {x['step']}"
            for x in read("plans.json")
        )

    return None

def local(q):
    memories = read("memory.json")

    memory_text = ""
    if memories:
        memory_text = "\n\n💾 MEMORY:\n" + "\n".join(
            "- " + str(x) for x in memories[-10:]
        )

    prompt = f"""Bạn là AI Lý Tưởng Sống.
Hãy trả lời bằng tiếng Việt, ngắn gọn và hữu ích.
{memory_text}

Câu hỏi của người dùng:
{q}
"""

    r = subprocess.run(
        [LLAMA, "-m", MODEL, "-c", "2048", "-n", "200", "-p", prompt],
        capture_output=True,
        text=True
    )
    return r.stdout.strip()

def online(q):
    env = "config/.env"
    key = ""

    if os.path.exists(env):
        with open(env, encoding="utf-8") as f:
            for line in f:
                if line.startswith("OPENAI_API_KEY="):
                    key = line.strip().split("=", 1)[1]

    if not key:
        return "☁️ Online chưa sẵn sàng: chưa có API key."

    data = json.dumps({
        "model": "gpt-5-mini",
        "input": q
    }).encode()

    req = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=data,
        headers={
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode())
        return result.get("output_text", "")
    except Exception as e:
        return "☁️ Online lỗi: " + str(e)

def route(q):
    if tool(q):
        return "TOOL"

    if len(q) > 200:
        return "ONLINE"

    return "LOCAL"

print("=" * 55)
print("🏭 LÝ TƯỞNG SỐNG CORE v1.1")
print("📱 Local + ☁️ Online + 🛠️ Tools")
print("=" * 55)
print("Gõ 'thoat' để đóng.\n")

while True:
    q = input("👤 Bạn: ").strip()

    if q.lower() == "thoat":
        print("👋 Đóng Core.")
        break

    if not q:
        continue

    destination = route(q)
    print("🔀 Router →", destination)

    if destination == "TOOL":
        print(tool(q))

    elif destination == "ONLINE":
        print("☁️ AI:", online(q))

    else:
        print("📱 AI:", local(q))

    print()
