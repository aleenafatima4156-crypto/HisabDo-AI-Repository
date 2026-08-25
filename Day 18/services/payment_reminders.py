import pandas as pd
from datetime import timedelta


def generate_payment_reminders(data):

    required_columns = [
        "payment_type",
        "payment_date",
        "amount"
    ]

    # Check required columns
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
    data["payment_date"] = pd.to_datetime(
        data["payment_date"],
        errors="coerce"
    )

    # Convert amount
    data["amount"] = pd.to_numeric(
        data["amount"],
        errors="coerce"
    )

    # Remove invalid records
    data = data.dropna(
        subset=["payment_date", "amount"]
    )

    if data.empty:
        return {
            "status": "error",
            "message": "No valid payment data found."
        }

    reminders = []

    # Analyze each payment type
    for payment_type, group in data.groupby("payment_type"):

        group = group.sort_values("payment_date")

        dates = group["payment_date"].tolist()

        # Need at least 2 payments to predict
        if len(dates) < 2:
            continue

        intervals = []

        for i in range(1, len(dates)):

            days = (
                dates[i] - dates[i - 1]
            ).days

            intervals.append(days)

        average_interval = sum(intervals) / len(intervals)

        last_payment = dates[-1]

        predicted_date = (
            last_payment +
            timedelta(days=round(average_interval))
        )

        reminders.append({
            "payment_type": payment_type,
            "last_payment_date": last_payment.strftime("%Y-%m-%d"),
            "average_interval_days": round(average_interval, 2),
            "predicted_next_payment": predicted_date.strftime("%Y-%m-%d"),
            "message": (
                f"{payment_type} payment is expected around "
                f"{predicted_date.strftime('%Y-%m-%d')}."
            )
        })

    if not reminders:

        return {
            "status": "success",
            "reminders": [],
            "message": (
                "Not enough payment history to make predictions."
            )
        }

    return {
        "status": "success",
        "reminders": reminders
    }