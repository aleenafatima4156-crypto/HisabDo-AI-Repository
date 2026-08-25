def generate_customer_risk_signal(data):

    required_fields = [
        "customer_id",
        "average_purchase_interval",
        "days_since_last_purchase",
        "pending_payment"
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

    try:
        average_interval = float(
            data["average_purchase_interval"]
        )

        days_since_purchase = float(
            data["days_since_last_purchase"]
        )

        pending_payment = float(
            data["pending_payment"]
        )

    except (ValueError, TypeError):

        return {
            "status": "error",
            "message": "Customer risk values must be valid numbers."
        }

    if average_interval <= 0:

        return {
            "status": "error",
            "message": (
                "Average purchase interval must be greater than zero."
            )
        }

    if days_since_purchase < 0:

        return {
            "status": "error",
            "message": "Days since last purchase cannot be negative."
        }

    if pending_payment < 0:

        return {
            "status": "error",
            "message": "Pending payment cannot be negative."
        }

    # --------------------------------
    # Inactivity ratio
    # --------------------------------

    inactivity_ratio = (
        days_since_purchase / average_interval
    )

    # --------------------------------
    # Inactivity signal
    # --------------------------------

    if inactivity_ratio >= 2:

        inactivity_signal = "HIGH"

    elif inactivity_ratio >= 1.25:

        inactivity_signal = "MEDIUM"

    else:

        inactivity_signal = "LOW"

    # --------------------------------
    # Payment signal
    # --------------------------------

    if pending_payment >= 50000:

        payment_signal = "HIGH"

    elif pending_payment > 0:

        payment_signal = "MEDIUM"

    else:

        payment_signal = "LOW"

    # --------------------------------
    # Score
    # --------------------------------

    risk_score = 0

    if inactivity_signal == "HIGH":
        risk_score += 60

    elif inactivity_signal == "MEDIUM":
        risk_score += 35

    else:
        risk_score += 10

    if payment_signal == "HIGH":
        risk_score += 40

    elif payment_signal == "MEDIUM":
        risk_score += 20

    else:
        risk_score += 0

    risk_score = min(risk_score, 100)

    # --------------------------------
    # Overall risk
    # --------------------------------

    if risk_score >= 70:

        risk_level = "HIGH"

    elif risk_score >= 40:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    # --------------------------------
    # Reasons
    # --------------------------------

    reasons = []

    if inactivity_signal == "HIGH":

        reasons.append(
            "Customer inactivity is significantly longer "
            "than the usual purchase interval."
        )

    elif inactivity_signal == "MEDIUM":

        reasons.append(
            "Customer inactivity is longer than "
            "the usual purchase interval."
        )

    if payment_signal == "HIGH":

        reasons.append(
            "Customer has a relatively high pending payment."
        )

    elif payment_signal == "MEDIUM":

        reasons.append(
            "Customer has an outstanding payment."
        )

    if not reasons:

        reasons.append(
            "No significant risk signal was detected "
            "from the provided activity."
        )

    # --------------------------------
    # Suggested action
    # --------------------------------

    if risk_level == "HIGH":

        suggested_action = (
            "Review the customer account and consider "
            "a polite follow-up regarding recent activity "
            "or outstanding payment."
        )

    elif risk_level == "MEDIUM":

        suggested_action = (
            "Monitor the customer and consider a follow-up "
            "if the inactivity or payment issue continues."
        )

    else:

        suggested_action = (
            "No immediate action is required. "
            "Continue monitoring normal customer activity."
        )

    return {
        "status": "success",

        "customer_id": data["customer_id"],

        "risk_score": risk_score,

        "risk_level": risk_level,

        "signals": {
            "inactivity": inactivity_signal,
            "payment": payment_signal
        },

        "metrics": {
            "average_purchase_interval": round(
                average_interval,
                2
            ),
            "days_since_last_purchase": round(
                days_since_purchase,
                2
            ),
            "inactivity_ratio": round(
                inactivity_ratio,
                2
            ),
            "pending_payment": round(
                pending_payment,
                2
            )
        },

        "reasons": reasons,

        "suggested_action": suggested_action
    }