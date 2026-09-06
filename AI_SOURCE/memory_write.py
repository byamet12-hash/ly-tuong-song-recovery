import json
import os
from datetime import datetime

FILE = "memory.json"

def load():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def remember(text):
    data = load()

    data.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "content": text
    })

    save(data)
    print("💾 Đã ghi Memory.")

print("💾 MEMORY WRITE v2.1")

text = input("🧠 Nội dung cần nhớ: ").strip()

if text:
    remember(text)
else:
    print("⚠️ Không có nội dung.")
