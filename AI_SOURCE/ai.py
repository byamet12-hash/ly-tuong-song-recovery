from datetime import datetime

print("=" * 45)
print("🤖 AI LÝ TƯỞNG SỐNG v0.1")
print("=" * 45)
print("Gõ 'thoat' để đóng Xưởng.\n")

while True:
    cau_hoi = input("👤 Bạn: ").strip()

    if cau_hoi.lower() == "thoat":
        print("👋 Tạm biệt! Xưởng vẫn ở đây.")
        break

    if not cau_hoi:
        continue

    q = cau_hoi.lower()

    if "xin chào" in q or "hello" in q:
        tra_loi = "Xin chào! Tôi là AI Lý Tưởng Sống v0.1 🤖"

    elif "python" in q:
        tra_loi = "Python là ngôn ngữ lập trình chúng ta đang dùng để xây Xưởng."

    elif "mục tiêu" in q:
        tra_loi = "Hãy xác định một mục tiêu rõ ràng, sau đó chia thành những hành động nhỏ."

    elif "thời gian" in q:
        tra_loi = "Bây giờ là " + datetime.now().strftime("%H:%M:%S - %d/%m/%Y")

    elif "bạn là ai" in q:
        tra_loi = "Tôi là phiên bản thử nghiệm của AI Lý Tưởng Sống."

    else:
        tra_loi = (
            "Tôi đã nhận câu hỏi: "
            + cau_hoi
            + "\nĐây là phiên bản v0.1; bộ não AI lớn sẽ được kết nối ở bước tiếp theo."
        )

    print("🤖 AI:", tra_loi)
    print()
