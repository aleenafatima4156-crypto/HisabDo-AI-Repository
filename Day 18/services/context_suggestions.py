import pandas as pd


def generate_context_aware_suggestion(
    current_expense,
    recent_expenses
):

    # Validate current expense
    if not current_expense:
        return {
            "status": "error",
            "message": "Current expense is required."
        }

    required_fields = [
        "expense",
        "amount",
        "category"
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in current_expense
    ]

    if missing_fields:
        return {
            "status": "error",
            "message": "Missing current expense fields.",
            "missing_fields": missing_fields
        }

    # Current expense information
    expense_name = current_expense["expense"]
    amount = pd.to_numeric(
        current_expense["amount"],
        errors="coerce"
    )
    category = current_expense["category"]

    if pd.isna(amount):
        return {
            "status": "error",
            "message": "Expense amount must be a valid number."
        }

    # Convert recent expenses to DataFrame
    recent_df = pd.DataFrame(recent_expenses)

    if recent_df.empty:
        return {
            "status": "success",
            "suggestion": (
                f"You recorded a new {category} expense of "
                f"PKR {amount:.2f}. Continue monitoring your spending."
            )
        }

    # Validate columns
    required_recent_columns = [
        "amount",
        "category"
    ]

    missing_recent = [
        column
        for column in required_recent_columns
        if column not in recent_df.columns
    ]

    if missing_recent:
        return {
            "status": "error",
            "message": "Recent expense data is incomplete.",
            "missing_fields": missing_recent
        }

    recent_df["amount"] = pd.to_numeric(
        recent_df["amount"],
        errors="coerce"
    )

    recent_df = recent_df.dropna(
        subset=["amount"]
    )

    # Recent spending for current category
    category_expenses = recent_df[
        recent_df["category"] == category
    ]

    recent_category_total = category_expenses["amount"].sum()

    # Average recent expense
    if not category_expenses.empty:
        average_category_expense = (
            category_expenses["amount"].mean()
        )
    else:
        average_category_expense = 0

    # --------------------------------
    # Generate context-aware suggestion
    # --------------------------------

    if (
        recent_category_total > 0
        and amount > average_category_expense * 2
    ):

        suggestion = (
            f"This {category} expense of PKR {amount:.2f} "
            f"is significantly higher than your recent average "
            f"{category} expense of "
            f"PKR {average_category_expense:.2f}. "
            "Consider reviewing this expense."
        )

        alert_level = "HIGH"

    elif (
        recent_category_total > 0
        and amount > average_category_expense
    ):

        suggestion = (
            f"Your new {category} expense is above your "
            "recent average. Keep monitoring this category."
        )

        alert_level = "MEDIUM"

    elif category_expenses.empty:

        suggestion = (
            f"This is a new spending category for your recent "
            f"history. Monitor your {category} expenses "
            "to understand your spending pattern."
        )

        alert_level = "LOW"

    else:

        suggestion = (
            f"Your new {category} expense appears to be "
            "within your recent spending pattern."
        )

        alert_level = "LOW"

    return {
        "status": "success",
        "current_expense": {
            "expense": expense_name,
            "amount": round(float(amount), 2),
            "category": category
        },
        "recent_category_spending": round(
            float(recent_category_total),
            2
        ),
        "recent_average_expense": round(
            float(average_category_expense),
            2
        ),
        "alert_level": alert_level,
        "suggestion": suggestion
    }