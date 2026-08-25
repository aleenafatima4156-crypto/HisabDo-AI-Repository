def generate_daily_business_brief(data):

    sales = float(data.get("sales", 0))
    expenses = float(data.get("expenses", 0))
    customers = int(data.get("customers", 0))
    pending_payments = int(data.get("pending_payments", 0))

    # Calculate profit
    profit = sales - expenses

    # Calculate profit margin
    if sales > 0:
        profit_margin = (profit / sales) * 100
    else:
        profit_margin = 0

    # Determine business status
    if profit > 0 and profit_margin >= 30:
        status = "Healthy"

    elif profit > 0:
        status = "Positive"

    elif profit == 0:
        status = "Break-even"

    else:
        status = "Needs Attention"

    # Generate insight
    if profit < 0:

        insight = (
            "Today's expenses are higher than sales. "
            "Review unnecessary expenses and monitor cash flow."
        )

    elif pending_payments >= 10:

        insight = (
            "Your business is generating positive results, "
            "but several payments are still pending. "
            "Follow up on outstanding payments."
        )

    elif profit_margin >= 30:

        insight = (
            "Today's business performance looks strong. "
            "Sales are generating a healthy profit margin."
        )

    else:

        insight = (
            "Today's business performance is positive. "
            "Continue monitoring sales and expenses."
        )

    return {
        "status": "success",
        "daily_summary": {
            "sales": round(sales, 2),
            "expenses": round(expenses, 2),
            "profit": round(profit, 2),
            "profit_margin": round(profit_margin, 2),
            "customers": customers,
            "pending_payments": pending_payments,
            "business_status": status
        },
        "ai_insight": insight
    }