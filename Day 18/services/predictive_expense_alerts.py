def generate_predictive_expense_alert(data):

    required_fields = [
        "category",
        "historical_monthly_spending",
        "current_spending"
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in data
    ]

    if missing_fields:
        return {
            "status": "error",
            "message": "Missing required fields.",
            "missing_fields": missing_fields
        }

    category = data["category"]
    historical = data["historical_monthly_spending"]
    current_spending = data["current_spending"]

    # Validate historical data
    if not isinstance(historical, list) or len(historical) < 2:

        return {
            "status": "error",
            "message": (
                "At least two historical monthly values "
                "are required."
            )
        }

    try:

        historical = [
            float(value)
            for value in historical
        ]

        current_spending = float(current_spending)

    except (ValueError, TypeError):

        return {
            "status": "error",
            "message": "Spending values must be valid numbers."
        }

    if any(value < 0 for value in historical):

        return {
            "status": "error",
            "message": "Historical spending cannot be negative."
        }

    if current_spending < 0:

        return {
            "status": "error",
            "message": "Current spending cannot be negative."
        }

    # --------------------------------
    # Historical average
    # --------------------------------

    historical_average = (
        sum(historical) / len(historical)
    )

    # --------------------------------
    # Calculate deviation
    # --------------------------------

    if historical_average > 0:

        deviation_percentage = (
            (current_spending - historical_average)
            / historical_average
        ) * 100

    else:

        deviation_percentage = 0

    # --------------------------------
    # Predictive alert
    # --------------------------------

    if deviation_percentage >= 30:

        alert_level = "HIGH"

        message = (
            f"{category} spending is currently "
            f"{deviation_percentage:.1f}% above your "
            "historical monthly average."
        )

        recommendation = (
            "Monitor this category closely and review "
            "recent expenses to avoid further increases."
        )

    elif deviation_percentage >= 15:

        alert_level = "MEDIUM"

        message = (
            f"{category} spending is moderately above "
            f"your historical monthly average "
            f"by {deviation_percentage:.1f}%."
        )

        recommendation = (
            "Keep monitoring this category during "
            "the rest of the month."
        )

    elif deviation_percentage > 0:

        alert_level = "LOW"

        message = (
            f"{category} spending is slightly above "
            "your historical pattern."
        )

        recommendation = (
            "Continue monitoring your spending."
        )

    else:

        alert_level = "NORMAL"

        message = (
            f"{category} spending is currently within "
            "or below your historical spending pattern."
        )

        recommendation = (
            "No immediate action is required."
        )

    # --------------------------------
    # Trend
    # --------------------------------

    if len(historical) >= 2:

        last_month = historical[-1]
        previous_month = historical[-2]

        if last_month > previous_month:

            trend = "Increasing"

        elif last_month < previous_month:

            trend = "Decreasing"

        else:

            trend = "Stable"

    else:

        trend = "Unknown"

    return {

        "status": "success",

        "category": category,

        "historical_average": round(
            historical_average,
            2
        ),

        "current_spending": round(
            current_spending,
            2
        ),

        "deviation_percentage": round(
            deviation_percentage,
            2
        ),

        "trend": trend,

        "alert_level": alert_level,

        "message": message,

        "recommendation": recommendation
    }