def approve(action):
    print("\n🛡️ APPROVAL ENGINE")
    print("⚙️ Hành động:", action)

    answer = input("👤 Bạn có duyệt? (y/n): ").strip().lower()

    if answer == "y":
        print("✅ Đã duyệt.")
        return True

    print("🛑 Đã từ chối.")
    return False


action = input("⚙️ Nhập hành động cần duyệt: ").strip()

if action:
    approve(action)
