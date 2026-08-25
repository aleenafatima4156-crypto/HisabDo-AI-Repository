def get_feature_guidance(data):

    feature = data.get("feature", "").strip().lower()

    if not feature:
        return {
            "status": "error",
            "message": "Feature name is required."
        }

    features = {

        "monthly insights": {
            "feature_name": "Monthly Insights",
            "location": "Dashboard → Insights → Monthly Insights",
            "steps": [
                "Open the HisabDo Dashboard.",
                "Open the Insights section.",
                "Select Monthly Insights.",
                "Review your monthly spending and financial summary."
            ],
            "description": (
                "Monthly Insights helps you understand "
                "your monthly financial activity."
            )
        },

        "expense categorization": {
            "feature_name": "Smart Expense Categorization",
            "location": "Expenses → Add Expense",
            "steps": [
                "Open the Expenses section.",
                "Select Add Expense.",
                "Enter your expense description.",
                "Submit the expense.",
                "Review the suggested category."
            ],
            "description": (
                "AI automatically suggests a suitable "
                "category for your expense."
            )
        },

        "financial goals": {
            "feature_name": "Financial Goal Tracking",
            "location": "Dashboard → Financial Goals",
            "steps": [
                "Open the Dashboard.",
                "Open Financial Goals.",
                "Create a new financial goal.",
                "Enter your target amount.",
                "Track your progress over time."
            ],
            "description": (
                "Financial Goal Tracking helps you monitor "
                "progress toward a financial target."
            )
        },

        "business health": {
            "feature_name": "Business Health Score",
            "location": "Dashboard → Business Health",
            "steps": [
                "Open the Dashboard.",
                "Open Business Health.",
                "Review your health score.",
                "Check the score breakdown and AI insight."
            ],
            "description": (
                "Business Health Score provides an overall "
                "view of business performance."
            )
        },

        "payment reminders": {
            "feature_name": "Payment Reminders",
            "location": "Payments → Reminders",
            "steps": [
                "Open the Payments section.",
                "Open Reminders.",
                "Review upcoming payments.",
                "Check payment due dates."
            ],
            "description": (
                "Payment Reminders help you keep track "
                "of upcoming payments."
            )
        }
    }

    result = features.get(feature)

    if not result:

        return {
            "status": "success",
            "feature_found": False,
            "message": (
                "I could not find that feature. "
                "Please provide a valid HisabDo feature name."
            )
        }

    return {
        "status": "success",
        "feature_found": True,
        "feature": result
    }