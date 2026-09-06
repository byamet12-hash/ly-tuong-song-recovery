import os

print("=" * 45)
print("🤖 AI LÝ TƯỞNG SỐNG v0.2")
print("=" * 45)
print("Đây là bộ khung AI mới.")
print("Gõ 'thoat' để đóng.\n")

while True:
    question = input("👤 Bạn: ").strip()

    if question.lower() == "thoat":
        print("👋 Đóng Xưởng.")
        break

    if not question:
        continue

    print("🤖 AI: Tôi đã nhận:", question)
    print("🧠 Bộ não AI thật sẽ được kết nối ở bước tiếp theo.\n")
