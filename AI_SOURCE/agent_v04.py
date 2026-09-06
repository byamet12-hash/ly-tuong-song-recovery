import json
import os
import subprocess

MODEL = "models/qwen2.5-1.5b-instruct-q4_k_m.gguf"
LLAMA = "llama.cpp/build/bin/llama-cli"
MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def remember(text):
    memory = load_memory()
    memory.append(text)
    save_memory(memory)

def ask_ai(question):
    memory = load_memory()

    recent_memory = "\n".join(
        f"- {item}" for item in memory[-10:]
    )

    prompt = f"""Bạn là AI Agent của dự án Lý Tưởng Sống.
Trả lời bằng tiếng Việt, rõ ràng, ngắn gọn và hữu ích.

TRÍ NHỚ:
{recent_memory if recent_memory else "- Chưa có trí nhớ."}

CÂU HỎI:
{question}

AI:"""

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

    return result.stdout.strip()

print("=" * 55)
print("🤖 AI AGENT LÝ TƯỞNG SỐNG v0.4")
print("🧠 Qwen Local + 💾 Memory")
print("=" * 55)
print("Lệnh đặc biệt:")
print("  nhớ: nội dung  → lưu vào Memory")
print("  xem             → xem Memory")
print("  thoat           → đóng Agent\n")

while True:
    question = input("👤 Bạn: ").strip()

    if question.lower() == "thoat":
        print("👋 Đóng Agent.")
        break

    if question.lower() == "xem":
        memory = load_memory()
        print("\n💾 MEMORY:")
        if memory:
            for i, item in enumerate(memory, 1):
                print(f"{i}. {item}")
        else:
            print("Memory đang trống.")
        print()
        continue

    if question.lower().startswith("nhớ:"):
        text = question[4:].strip()

        if text:
            remember(text)
            print("💾 Đã ghi nhớ.\n")
        continue

    if not question:
        continue

    print("\n🤖 AI:", ask_ai(question))
    print()
