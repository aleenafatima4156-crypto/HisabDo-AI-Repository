def generate_step_help(data):

    task = data.get("task", "").strip().lower()

    if not task:
        return {
            "status": "error",
            "message": "Task name is required."
        }

    tasks = {

        "add expense": {
            "task_name": "Add an Expense",
            "steps": [
                "Open the Expenses section.",
                "Select Add Expense.",
                "Enter the expense description.",
                "Enter the expense amount.",
                "Select or review the expense category.",
                "Check the entered information.",
                "Click Save to record the expense.",
                "Confirm that the expense was added successfully."
            ]
        },

        "create financial goal": {
            "task_name": "Create a Financial Goal",
            "steps": [
                "Open the Financial Goals section.",
                "Select Create Goal.",
                "Enter a name for your goal.",
                "Enter the target amount.",
                "Enter or confirm the current saved amount.",
                "Review the goal information.",
                "Save the financial goal.",
                "Monitor your progress from the Financial Goals section."
            ]
        },

        "check monthly insights": {
            "task_name": "Check Monthly Insights",
            "steps": [
                "Open the HisabDo Dashboard.",
                "Open the Insights section.",
                "Select Monthly Insights.",
                "Review your monthly income and expenses.",
                "Review spending by category.",
                "Check the generated financial insights.",
                "Use the insights to understand your monthly spending pattern."
            ]
        },

        "check business health": {
            "task_name": "Check Business Health",
            "steps": [
                "Open the Dashboard.",
                "Open the Business Health section.",
                "Review the overall health score.",
                "Check the profitability information.",
                "Review customer activity.",
                "Check pending payments.",
                "Review the AI-generated business insight."
            ]
        },

        "check payment reminders": {
            "task_name": "Check Payment Reminders",
            "steps": [
                "Open the Payments section.",
                "Open Payment Reminders.",
                "Review upcoming payments.",
                "Check the payment due dates.",
                "Review any overdue payments.",
                "Take the required payment action."
            ]
        }
    }

    result = tasks.get(task)

    if not result:
        return {
            "status": "success",
            "task_found": False,
            "message": (
                "I could not find instructions for this task. "
                "Please provide a supported HisabDo task."
            )
        }

    return {
        "status": "success",
        "task_found": True,
        "task": result["task_name"],
        "total_steps": len(result["steps"]),
        "steps": result["steps"]
    }