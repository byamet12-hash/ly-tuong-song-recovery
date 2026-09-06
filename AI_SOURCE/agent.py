import subprocess

MODEL = "models/qwen2.5-1.5b-instruct-q4_k_m.gguf"
LLAMA = "llama.cpp/build/bin/llama-cli"

print("=" * 50)
print("🤖 AI AGENT LÝ TƯỞNG SỐNG v0.3")
print("=" * 50)
print("🧠 Bộ não: Qwen Local")
print("Gõ 'thoat' để đóng.\n")

while True:
    question = input("👤 Bạn: ").strip()

    if question.lower() == "thoat":
        print("👋 Đóng Agent.")
        break

    if not question:
        continue

    prompt = f"""Bạn là AI Agent của dự án Lý Tưởng Sống.
Hãy trả lời bằng tiếng Việt, rõ ràng và hữu ích.

Người dùng hỏi:
{question}

AI Agent:"""

    try:
        result = subprocess.run(
            [
                LLAMA,
                "-m", MODEL,
                "-c", "1024",
                "-n", "256",
                "-p", prompt
            ],
            capture_output=True,
            text=True
        )

        print("\n🤖 AI:", result.stdout.strip(), "\n")

    except Exception as e:
        print("⚠️ Lỗi:", e)
