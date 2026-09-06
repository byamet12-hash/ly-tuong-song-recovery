def choose_agent(task):
    q = task.lower()

    if any(x in q for x in ["mục tiêu", "goal", "tiến độ"]):
        return "🎯 Goal Agent"

    if any(x in q for x in ["kế hoạch", "plan", "bước"]):
        return "📋 Planning Agent"

    if any(x in q for x in ["nhớ", "memory", "ghi nhớ"]):
        return "💾 Memory Agent"

    if any(x in q for x in ["tính", "calculate", "toán"]):
        return "🧮 Calculation Tool"

    return "🧠 Local AI Agent"


print("=" * 55)
print("🤖 ORCHESTRATOR LÝ TƯỞNG SỐNG v0.9")
print("=" * 55)
print("Gõ 'thoat' để đóng.\n")

while True:
    task = input("👤 Nhiệm vụ: ").strip()

    if task.lower() == "thoat":
        print("👋 Đóng Orchestrator.")
        break

    if not task:
        continue

    agent = choose_agent(task)

    print("🔀 Orchestrator →", agent)
    print("✅ Đã phân công.\n")
