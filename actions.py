def execute_action(response):
    if "transfer" in response.lower():
        print("💸 Simulating fund transfer...")
    elif "report" in response.lower():
        print("📊 Generating report...")
    else:
        print("⚙️ No recognizable action. Awaiting clarification.")