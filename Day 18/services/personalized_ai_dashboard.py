def generate_ai_dashboard(data):

    required_fields = [
        "business_health",
        "monthly_insights"
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in data
    ]

    if missing_fields:

        return {
            "status": "error",
            "message": "Dashboard data is incomplete.",
            "missing_fields": missing_fields
        }

    business_health = data.get(
        "business_health",
        {}
    )

    monthly_insights = data.get(
        "monthly_insights",
        {}
    )

    financial_goal = data.get(
        "financial_goal"
    )

    notifications = data.get(
        "notifications",
        []
    )

    customer_risks = data.get(
        "customer_risks",
        []
    )

    recommendations = data.get(
        "recommendations",
        []
    )

    # --------------------------------
    # Business Health
    # --------------------------------

    health_score = business_health.get(
        "health_score",
        0
    )

    health_status = business_health.get(
        "business_status",
        "Unknown"
    )

    # --------------------------------
    # Monthly Summary
    # --------------------------------

    monthly_summary = monthly_insights.get(
        "summary",
        {}
    )

    income = monthly_summary.get(
        "income",
        0
    )

    expenses = monthly_summary.get(
        "expenses",
        0
    )

    profit = monthly_summary.get(
        "profit",
        0
    )

    savings_rate = monthly_summary.get(
        "savings_rate",
        0
    )

    # --------------------------------
    # Goal
    # --------------------------------

    goal_summary = None

    if isinstance(financial_goal, dict):

        target = financial_goal.get(
            "target",
            0
        )

        current = financial_goal.get(
            "current",
            0
        )

        try:

            target = float(target)
            current = float(current)

        except (ValueError, TypeError):

            target = 0
            current = 0

        if target > 0:

            goal_progress = (
                current / target
            ) * 100

            goal_progress = min(
                goal_progress,
                100
            )

        else:

            goal_progress = 0

        goal_summary = {
            "name": financial_goal.get(
                "name",
                "Financial Goal"
            ),
            "target": target,
            "current": current,
            "progress_percentage": round(
                goal_progress,
                2
            )
        }

    # --------------------------------
    # Notifications
    # --------------------------------

    if not isinstance(notifications, list):

        notifications = []

    important_notifications = []

    for notification in notifications:

        if not isinstance(notification, dict):
            continue

        priority = str(
            notification.get(
                "priority",
                "LOW"
            )
        ).upper()

        if priority in [
            "CRITICAL",
            "HIGH"
        ]:

            important_notifications.append(
                notification
            )

    # --------------------------------
    # Customer Risks
    # --------------------------------

    if not isinstance(customer_risks, list):

        customer_risks = []

    high_risk_customers = []

    for customer in customer_risks:

        if not isinstance(customer, dict):
            continue

        risk_level = str(
            customer.get(
                "risk_level",
                "LOW"
            )
        ).upper()

        if risk_level == "HIGH":

            high_risk_customers.append(
                customer
            )

    # --------------------------------
    # Top Recommendation
    # --------------------------------

    top_recommendation = None

    if isinstance(recommendations, list):

        for recommendation in recommendations:

            if isinstance(recommendation, str):

                top_recommendation = recommendation
                break

            if isinstance(recommendation, dict):

                top_recommendation = recommendation
                break

    # --------------------------------
    # Dashboard Status
    # --------------------------------

    if health_score >= 80:

        dashboard_status = "Healthy"

    elif health_score >= 60:

        dashboard_status = "Stable"

    elif health_score >= 40:

        dashboard_status = "Needs Attention"

    else:

        dashboard_status = "At Risk"

    # --------------------------------
    # AI Summary
    # --------------------------------

    if profit < 0:

        ai_summary = (
            "Your business is currently operating "
            "below profitability. Review expenses "
            "and prioritize cost control."
        )

    elif len(important_notifications) > 0:

        ai_summary = (
            "Your business is profitable, but "
            "there are important alerts that "
            "should be reviewed."
        )

    elif len(high_risk_customers) > 0:

        ai_summary = (
            "Overall business performance is positive, "
            "but some customers may require follow-up."
        )

    elif health_score >= 80:

        ai_summary = (
            "Your business is performing strongly. "
            "Continue monitoring expenses, goals, "
            "and customer activity."
        )

    else:

        ai_summary = (
            "Business performance is moderate. "
            "Continue monitoring key financial indicators."
        )

    # --------------------------------
    # Final Dashboard
    # --------------------------------

    return {

        "status": "success",

        "dashboard_status": dashboard_status,

        "business_health": {
            "score": health_score,
            "status": health_status
        },

        "monthly_financials": {
            "income": income,
            "expenses": expenses,
            "profit": profit,
            "savings_rate": savings_rate
        },

        "financial_goal": goal_summary,

        "alerts": {
            "total": len(notifications),
            "important": len(
                important_notifications
            ),
            "items": important_notifications
        },

        "customer_risk": {
            "total_customers_analyzed": len(
                customer_risks
            ),
            "high_risk_customers": len(
                high_risk_customers
            ),
            "items": high_risk_customers
        },

        "top_recommendation": top_recommendation,

        "ai_summary": ai_summary
    }