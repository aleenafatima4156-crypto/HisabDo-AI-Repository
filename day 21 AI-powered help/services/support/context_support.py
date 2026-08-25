def generate_context_help(data):

    user_query = data.get("user_query", "").strip()
    page = data.get("page", "").strip().lower()
    action = data.get("action", "").strip().lower()

    if not user_query:
        return {
            "status": "error",
            "message": "User query is required."
        }

    # Expense page
    if page == "expense_entry":

        if action == "adding_expense":
            response = (
                "To add an expense, enter the expense description, "
                "amount and category, then save the transaction."
            )

        elif action == "selecting_category":
            response = (
                "Choose the category that best matches your expense. "
                "For example, groceries can be categorized as "
                "Food & Groceries."
            )

        else:
            response = (
                "You are currently on the Expense Entry page. "
                "You can add a description, amount and category "
                "for your expense."
            )

    # Dashboard page
    elif page == "dashboard":

        response = (
            "You are on the Dashboard. Here you can review your "
            "financial summary, spending patterns, alerts and insights."
        )

    # Payment page
    elif page == "payments":

        response = (
            "You are on the Payments page. You can review payment "
            "records, upcoming payments and payment status."
        )

    # Unknown context
    else:

        response = (
            "I can help you with HisabDo features. "
            "Tell me what you are trying to do and I will guide you."
        )

    return {
        "status": "success",
        "context": {
            "page": page,
            "action": action
        },
        "response": response
    }