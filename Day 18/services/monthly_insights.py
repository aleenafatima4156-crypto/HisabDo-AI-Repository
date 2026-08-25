from collections import defaultdict


def generate_monthly_insights(data):

    required_fields = [
        "month",
        "income",
        "expenses"
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

        income = float(data["income"])
        expenses = float(data["expenses"])

    except (ValueError, TypeError):

        return {
            "status": "error",
            "message": "Income and expenses must be valid numbers."
        }

    if income < 0 or expenses < 0:

        return {
            "status": "error",
            "message": "Income and expenses cannot be negative."
        }

    # --------------------------------
    # Basic calculations
    # --------------------------------

    profit = income - expenses

    if income > 0:

        savings_rate = (
            profit / income
        ) * 100

    else:

        savings_rate = 0

    # --------------------------------
    # Category analysis
    # --------------------------------

    categories = data.get(
        "category_expenses",
        []
    )

    category_totals = defaultdict(float)

    if isinstance(categories, list):

        for item in categories:

            if not isinstance(item, dict):
                continue

            category = item.get(
                "category"
            )

            amount = item.get(
                "amount",
                0
            )

            try:
                amount = float(amount)
            except (ValueError, TypeError):
                continue

            if category and amount >= 0:

                category_totals[category] += amount

    # --------------------------------
    # Top category
    # --------------------------------

    if category_totals:

        top_category = max(
            category_totals,
            key=category_totals.get
        )

        top_category_amount = (
            category_totals[top_category]
        )

    else:

        top_category = None
        top_category_amount = 0

    # --------------------------------
    # Monthly comparison
    # --------------------------------

    previous_month = data.get(
        "previous_month"
    )

    expense_change_percentage = None

    if previous_month:

        try:

            previous_expenses = float(
                previous_month.get(
                    "expenses",
                    0
                )
            )

            if previous_expenses > 0:

                expense_change_percentage = (
                    (expenses - previous_expenses)
                    / previous_expenses
                ) * 100

        except (ValueError, TypeError):

            expense_change_percentage = None

    # --------------------------------
    # Generate insights
    # --------------------------------

    insights = []

    # Profit insight
    if profit > 0:

        insights.append(
            f"Your business generated a positive "
            f"monthly result of PKR {profit:.2f}."
        )

    elif profit < 0:

        insights.append(
            f"Your expenses exceeded income by "
            f"PKR {abs(profit):.2f}."
        )

    else:

        insights.append(
            "Your income and expenses were equal this month."
        )

    # Savings insight
    if savings_rate >= 30:

        insights.append(
            f"Your savings/profit rate was "
            f"{savings_rate:.1f}%, which is relatively strong."
        )

    elif savings_rate > 0:

        insights.append(
            f"Your savings/profit rate was "
            f"{savings_rate:.1f}%."
        )

    else:

        insights.append(
            "There was no positive amount left after expenses."
        )

    # Top category insight
    if top_category:

        insights.append(
            f"{top_category} was your highest spending "
            f"category at PKR {top_category_amount:.2f}."
        )

    # Expense comparison
    if expense_change_percentage is not None:

        if expense_change_percentage > 10:

            insights.append(
                f"Expenses increased by "
                f"{expense_change_percentage:.1f}% "
                "compared with the previous month."
            )

        elif expense_change_percentage < -10:

            insights.append(
                f"Expenses decreased by "
                f"{abs(expense_change_percentage):.1f}% "
                "compared with the previous month."
            )

        else:

            insights.append(
                "Monthly expenses remained relatively "
                "stable compared with the previous month."
            )

    # --------------------------------
    # Recommendation
    # --------------------------------

    if profit < 0:

        recommendation = (
            "Review major expense categories and identify "
            "areas where spending can be reduced."
        )

    elif top_category and (
        top_category_amount > expenses * 0.30
    ):

        recommendation = (
            f"Consider reviewing your {top_category} "
            "expenses because this category represents "
            "a significant share of total spending."
        )

    elif expense_change_percentage is not None and (
        expense_change_percentage > 10
    ):

        recommendation = (
            "Monitor your expenses next month because "
            "spending increased compared with the previous month."
        )

    else:

        recommendation = (
            "Continue tracking income and expenses regularly "
            "to maintain visibility into your financial activity."
        )

    return {

        "status": "success",

        "month": data["month"],

        "summary": {
            "income": round(
                income,
                2
            ),
            "expenses": round(
                expenses,
                2
            ),
            "profit": round(
                profit,
                2
            ),
            "savings_rate": round(
                savings_rate,
                2
            )
        },

        "category_breakdown": {
            category: round(
                amount,
                2
            )
            for category, amount
            in category_totals.items()
        },

        "top_category": top_category,

        "top_category_amount": round(
            top_category_amount,
            2
        ),

        "expense_change_percentage": (
            round(
                expense_change_percentage,
                2
            )
            if expense_change_percentage is not None
            else None
        ),

        "insights": insights,

        "recommendation": recommendation
    }