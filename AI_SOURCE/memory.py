import json
import os

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

def add_memory(text):
    memory = load_memory()
    memory.append(text)
    save_memory(memory)

def show_memory():
    memory = load_memory()

    if not memory:
        print("💾 Memory đang trống.")
        return

    print("\n💾 TRÍ NHỚ:")
    for i, item in enumerate(memory, 1):
        print(f"{i}. {item}")
    print()

print("💾 MEMORY LÝ TƯỞNG SỐNG v0.1")
print("Gõ 'them: ...' để ghi nhớ")
print("Gõ 'xem' để xem trí nhớ")
print("Gõ 'thoat' để đóng\n")

while True:
    command = input("🧠 Memory: ").strip()

    if command.lower() == "thoat":
        break

    elif command.lower() == "xem":
        show_memory()

    elif command.lower().startswith("them:"):
        text = command[5:].strip()

        if text:
            add_memory(text)
            print("✅ Đã ghi nhớ.\n")
        else:
            print("⚠️ Chưa có nội dung.\n")

    else:
        print("Dùng: them: nội dung | xem | thoat")
