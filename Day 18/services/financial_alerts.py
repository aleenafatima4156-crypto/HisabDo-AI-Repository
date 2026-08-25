import pandas as pd


def generate_smart_financial_alerts(data):

    # Convert amount to numeric
    data["amount"] = pd.to_numeric(
        data["amount"],
        errors="coerce"
    )

    # Remove invalid amounts
    data = data.dropna(subset=["amount"])

    if data.empty:
        return {
            "status": "error",
            "message": "No valid expense data found."
        }

    total_spending = data["amount"].sum()

    alerts = []

    # --------------------------------
    # Alert 1: High Overall Spending
    # --------------------------------

    if total_spending >= 50000:

        alerts.append({
            "type": "HIGH_SPENDING",
            "priority": "HIGH",
            "message": (
                f"Your total spending is PKR {total_spending:.2f}. "
                "Your overall spending level is high."
            )
        })

    elif total_spending >= 30000:

        alerts.append({
            "type": "MODERATE_SPENDING",
            "priority": "MEDIUM",
            "message": (
                f"Your total spending is PKR {total_spending:.2f}. "
                "Keep monitoring your expenses."
            )
        })

    # --------------------------------
    # Alert 2: High Category Spending
    # --------------------------------

    if "category" in data.columns:

        category_spending = (
            data.groupby("category")["amount"]
            .sum()
            .sort_values(ascending=False)
        )

        for category, amount in category_spending.items():

            percentage = (amount / total_spending) * 100

            if percentage >= 40:

                alerts.append({
                    "type": "HIGH_CATEGORY_SPENDING",
                    "priority": "HIGH",
                    "category": category,
                    "amount": round(amount, 2),
                    "percentage": round(percentage, 2),
                    "message": (
                        f"{category} represents "
                        f"{percentage:.2f}% of your total spending."
                    )
                })

    # --------------------------------
    # No Alert
    # --------------------------------

    if not alerts:

        alerts.append({
            "type": "NORMAL",
            "priority": "LOW",
            "message": (
                "Your spending is currently within "
                "a normal range."
            )
        })

    return {
        "status": "success",
        "total_spending": round(total_spending, 2),
        "alerts": alerts
    }