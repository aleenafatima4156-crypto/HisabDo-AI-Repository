import pandas as pd
from datetime import datetime


def generate_customer_followup_suggestions(data):

    required_columns = [
        "customer_id",
        "purchase_date",
        "amount"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        return {
            "status": "error",
            "message": "Missing required fields.",
            "missing_fields": missing_columns
        }

    # Convert dates
    data["purchase_date"] = pd.to_datetime(
        data["purchase_date"],
        errors="coerce"
    )

    # Convert amount
    data["amount"] = pd.to_numeric(
        data["amount"],
        errors="coerce"
    )

    data = data.dropna(
        subset=[
            "customer_id",
            "purchase_date",
            "amount"
        ]
    )

    if data.empty:
        return {
            "status": "error",
            "message": "No valid customer data found."
        }

    suggestions = []

    today = pd.Timestamp(datetime.now().date())

    # Analyze each customer
    for customer_id, group in data.groupby("customer_id"):

        group = group.sort_values("purchase_date")

        dates = group["purchase_date"].tolist()

        # Need at least 2 purchases
        if len(dates) < 2:
            continue

        intervals = []

        for i in range(1, len(dates)):

            days = (
                dates[i] - dates[i - 1]
            ).days

            intervals.append(days)

        average_interval = sum(intervals) / len(intervals)

        last_purchase = dates[-1]

        days_since_purchase = (
            today - last_purchase
        ).days

        # Follow-up threshold
        threshold = average_interval * 1.25

        if days_since_purchase > threshold:

            priority = "HIGH"

            message = (
                f"Customer {customer_id} has been inactive "
                f"for {days_since_purchase} days, which is longer "
                f"than their usual purchase interval."
            )

            action = (
                "Consider sending a friendly follow-up "
                "or checking whether the customer needs assistance."
            )

        elif days_since_purchase > average_interval:

            priority = "MEDIUM"

            message = (
                f"Customer {customer_id} is approaching "
                f"a longer-than-usual gap between purchases."
            )

            action = (
                "Consider monitoring the customer and "
                "sending a follow-up if inactivity continues."
            )

        else:

            priority = "LOW"

            message = (
                f"Customer {customer_id} is currently "
                f"within their usual purchase pattern."
            )

            action = (
                "No immediate follow-up is needed."
            )

        suggestions.append({
            "customer_id": customer_id,
            "last_purchase": last_purchase.strftime("%Y-%m-%d"),
            "days_since_purchase": days_since_purchase,
            "average_purchase_interval": round(
                average_interval, 2
            ),
            "priority": priority,
            "message": message,
            "suggested_action": action
        })

    if not suggestions:

        return {
            "status": "success",
            "suggestions": [],
            "message": (
                "Not enough purchase history to generate suggestions."
            )
        }

    return {
        "status": "success",
        "suggestions": suggestions
    }