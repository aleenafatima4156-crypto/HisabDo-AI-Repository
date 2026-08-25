import pandas as pd


def generate_personalized_recommendation(data):

    data["amount"] = pd.to_numeric(
        data["amount"],
        errors="coerce"
    )

    data = data.dropna(subset=["amount"])

    if data.empty:
        return {
            "status": "error",
            "message": "No valid expense data found."
        }

    total_spending = data["amount"].sum()

    category_spending = (
        data.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    highest_category = category_spending.index[0]

    highest_amount = category_spending.iloc[0]

    percentage = (
        highest_amount / total_spending
    ) * 100

    if percentage >= 40:

        recommendation = (
            f"Your {highest_category} spending is relatively high. "
            f"It represents {percentage:.2f}% of your total spending. "
            f"Consider setting a budget for this category."
        )

    elif percentage >= 25:

        recommendation = (
            f"{highest_category} is your highest spending category "
            f"at {percentage:.2f}% of total spending. "
            f"Keep monitoring this category."
        )

    else:

        recommendation = (
            "Your spending is reasonably distributed across categories. "
            "Continue monitoring your expenses."
        )

    return {
        "status": "success",
        "total_spending": round(total_spending, 2),
        "top_category": highest_category,
        "top_category_spending": round(highest_amount, 2),
        "percentage": round(percentage, 2),
        "recommendation": recommendation
    }