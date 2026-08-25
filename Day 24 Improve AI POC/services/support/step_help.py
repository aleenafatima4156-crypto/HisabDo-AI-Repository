def generate_step_help(data):
    task = str(data.get("task", "")).strip()

    steps = {
        "add expense": [
            "Open the Expenses section.",
            "Select Add Expense.",
            "Enter the expense details.",
            "Review the information.",
            "Save the expense."
        ],
        "create invoice": [
            "Open the Invoices section.",
            "Select Create Invoice.",
            "Select the customer.",
            "Add products or services.",
            "Review and save the invoice."
        ]
    }

    return {
        "task": task,
        "steps": steps.get(
            task.lower(),
            [
                "Open the relevant feature.",
                "Select the required action.",
                "Enter the requested information.",
                "Review the information.",
                "Save or confirm the action."
            ]
        )
    }
