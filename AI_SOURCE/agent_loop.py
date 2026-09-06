from action_engine import suggest
from approval_engine import approve

print("🤖 AGENT LOOP v1.7")
print("=" * 40)

print("\n⚙️ Agent đang phân tích...")
suggest()

action = input("\n⚙️ Nhập hành động muốn Agent đề xuất: ").strip()

if action:
    if approve(action):
        print("🛠️ Thực thi:", action)
        print("✅ Agent Loop hoàn tất.")
    else:
        print("🛑 Agent dừng lại.")
