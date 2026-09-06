def route(q):
    q = q.lower()

    if any(x in q for x in ["mục tiêu", "goal", "kế hoạch",
                             "plan", "memory", "trí nhớ",
                             "tiến độ", "status"]):
        return "🛠️ TOOL"

    if len(q) > 200:
        return "☁️ ONLINE"

    return "📱 LOCAL"

print("🔀 AI ROUTER v0.9")
print("Gõ 'thoat' để đóng.\n")

while True:
    q = input("👤 Bạn: ").strip()

    if q.lower() == "thoat":
        print("👋 Đóng Router.")
        break

    if q:
        print("🔀 Chọn:", route(q))
