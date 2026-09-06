import json
import os
import urllib.request
import urllib.error

ENV_FILE = "config/.env"

def load_key():
    if not os.path.exists(ENV_FILE):
        return ""

    with open(ENV_FILE, encoding="utf-8") as f:
        for line in f:
            if line.startswith("OPENAI_API_KEY="):
                return line.strip().split("=", 1)[1]

    return ""

def ask_online(question):
    api_key = load_key()

    if not api_key:
        print("⚠️ Chưa có OPENAI_API_KEY trong config/.env")
        print("ℹ️ online.py đã sẵn sàng, nhưng chưa gọi API.")
        return

    url = "https://api.openai.com/v1/responses"

    data = {
        "model": "gpt-5-mini",
        "input": question
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))

        text = result.get("output_text", "")
        print("\n☁️ AI Online:", text)

    except urllib.error.HTTPError as e:
        print("❌ HTTP Error:", e.code)
        print(e.read().decode("utf-8", errors="ignore"))

    except Exception as e:
        print("❌ Lỗi kết nối:", e)

print("=" * 50)
print("☁️ AI ONLINE LÝ TƯỞNG SỐNG v0.1")
print("=" * 50)

question = input("👤 Bạn: ").strip()

if question:
    ask_online(question)
