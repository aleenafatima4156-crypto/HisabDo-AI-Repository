def calculate_business_health(data):

    required_fields = [
        "sales",
        "expenses",
        "customers",
        "pending_payments"
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
        sales = float(data["sales"])
        expenses = float(data["expenses"])
        customers = int(data["customers"])
        pending_payments = int(data["pending_payments"])

    except (ValueError, TypeError):

        return {
            "status": "error",
            "message": "All values must be valid numbers."
        }

    # -----------------------------
    # Validation
    # -----------------------------

    if sales < 0 or expenses < 0:
        return {
            "status": "error",
            "message": "Sales and expenses cannot be negative."
        }

    if customers < 0 or pending_payments < 0:
        return {
            "status": "error",
            "message": "Customers and pending payments cannot be negative."
        }

    # -----------------------------
    # Profit
    # -----------------------------

    profit = sales - expenses

    if sales > 0:
        profit_margin = (profit / sales) * 100
    else:
        profit_margin = 0

    # -----------------------------
    # Score: Profitability
    # Maximum = 40
    # -----------------------------

    if profit_margin >= 40:
        profitability_score = 40

    elif profit_margin >= 30:
        profitability_score = 35

    elif profit_margin >= 20:
        profitability_score = 30

    elif profit_margin >= 10:
        profitability_score = 20

    elif profit_margin > 0:
        profitability_score = 10

    else:
        profitability_score = 0

    # -----------------------------
    # Score: Customer Activity
    # Maximum = 20
    # -----------------------------

    if customers >= 50:
        customer_score = 20

    elif customers >= 30:
        customer_score = 16

    elif customers >= 15:
        customer_score = 12

    elif customers > 0:
        customer_score = 6

    else:
        customer_score = 0

    # -----------------------------
    # Score: Payment Collection
    # Maximum = 20
    # -----------------------------

    if pending_payments == 0:
        payment_score = 20

    elif pending_payments <= 3:
        payment_score = 16

    elif pending_payments <= 7:
        payment_score = 12

    elif pending_payments <= 10:
        payment_score = 6

    else:
        payment_score = 0

    # -----------------------------
    # Score: Expense Control
    # Maximum = 20
    # -----------------------------

    if sales > 0:

        expense_ratio = (
            expenses / sales
        ) * 100

    else:
        expense_ratio = 100

    if expense_ratio <= 40:
        expense_score = 20

    elif expense_ratio <= 50:
        expense_score = 16

    elif expense_ratio <= 60:
        expense_score = 12

    elif expense_ratio <= 75:
        expense_score = 6

    else:
        expense_score = 0

    # -----------------------------
    # Final Score
    # -----------------------------

    health_score = (
        profitability_score
        + customer_score
        + payment_score
        + expense_score
    )

    # -----------------------------
    # Business Status
    # -----------------------------

    if health_score >= 80:
        business_status = "Excellent"

    elif health_score >= 65:
        business_status = "Healthy"

    elif health_score >= 50:
        business_status = "Moderate"

    elif health_score >= 30:
        business_status = "Needs Attention"

    else:
        business_status = "Critical"

    # -----------------------------
    # Insight
    # -----------------------------

    if profit < 0:

        insight = (
            "Expenses are higher than sales. "
            "Review costs and monitor profitability."
        )

    elif pending_payments > 7:

        insight = (
            "Business profitability is positive, "
            "but pending payments require attention."
        )

    elif expense_ratio > 60:

        insight = (
            "Expenses represent a relatively large "
            "portion of sales. Review spending."
        )

    elif health_score >= 65:

        insight = (
            "Overall business performance looks healthy. "
            "Continue monitoring profitability and customer activity."
        )

    else:

        insight = (
            "Business performance is moderate. "
            "Focus on improving profitability and expense control."
        )

    return {
        "status": "success",
        "health_score": health_score,
        "business_status": business_status,

        "metrics": {
            "sales": round(sales, 2),
            "expenses": round(expenses, 2),
            "profit": round(profit, 2),
            "profit_margin": round(profit_margin, 2),
            "customers": customers,
            "pending_payments": pending_payments,
            "expense_ratio": round(expense_ratio, 2)
        },

        "score_breakdown": {
            "profitability": profitability_score,
            "customer_activity": customer_score,
            "payment_collection": payment_score,
            "expense_control": expense_score
        },

        "ai_insight": insight
    }