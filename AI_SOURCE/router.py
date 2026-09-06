def route(question):
    q = question.lower()

    if any(x in q for x in [
        "memory", "trí nhớ", "mục tiêu", "goal",
        "kế hoạch", "plan", "tiến độ", "status"
    ]):
        return "TOOL"

    if len(question) > 200:
        return "ONLINE"

    return "LOCAL"


print("=" * 50)
print("🔀 AI ROUTER LÝ TƯỞNG SỐNG v0.8")
print("=" * 50)
print("Gõ 'thoat' để đóng.\n")

while True:
    question = input("👤 Bạn: ").strip()

    if question.lower() == "thoat":
        print("👋 Đóng Router.")
        break

    if not question:
        continue

    destination = route(question)

    print("🔀 Router →", destination)
    print()
