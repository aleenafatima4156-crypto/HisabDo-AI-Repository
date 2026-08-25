def discover_features(data):

    total_expenses = int(data.get("total_expenses", 0))
    monthly_expenses = int(data.get("monthly_expenses", 0))
    categories_used = int(data.get("categories_used", 0))

    has_goal = bool(data.get("has_goal", False))
    has_monthly_insights = bool(
        data.get("has_monthly_insights", False)
    )
    has_budget = bool(
        data.get("has_budget", False)
    )

    suggestions = []

    # --------------------------------
    # Monthly Insights
    # --------------------------------

    if monthly_expenses >= 10 and not has_monthly_insights:

        suggestions.append({
            "feature": "Monthly Insights",
            "priority": "HIGH",
            "reason": (
                "You have recorded many expenses this month."
            ),
            "suggestion": (
                "Try Monthly Insights to understand "
                "your spending patterns."
            )
        })

    # --------------------------------
    # Financial Goal Tracking
    # --------------------------------

    if total_expenses >= 15 and not has_goal:

        suggestions.append({
            "feature": "Financial Goal Tracking",
            "priority": "MEDIUM",
            "reason": (
                "You are actively tracking your expenses."
            ),
            "suggestion": (
                "Set a financial goal and monitor "
                "your progress."
            )
        })

    # --------------------------------
    # Budget Feature
    # --------------------------------

    if categories_used >= 3 and not has_budget:

        suggestions.append({
            "feature": "Budget Tracking",
            "priority": "MEDIUM",
            "reason": (
                "You are spending across multiple categories."
            ),
            "suggestion": (
                "Create category-based budgets "
                "to control your spending."
            )
        })

    # --------------------------------
    # Personalized Recommendations
    # --------------------------------

    if total_expenses >= 5:

        suggestions.append({
            "feature": "Personalized Recommendations",
            "priority": "LOW",
            "reason": (
                "You have enough expense activity "
                "for personalized suggestions."
            ),
            "suggestion": (
                "Use AI recommendations to get "
                "spending advice based on your activity."
            )
        })

    # --------------------------------
    # No suggestions
    # --------------------------------

    if not suggestions:

        suggestions.append({
            "feature": "Getting Started",
            "priority": "LOW",
            "reason": "Your activity level is still low.",
            "suggestion": (
                "Continue recording expenses to unlock "
                "more personalized features."
            )
        })

    return {
        "status": "success",
        "suggestions": suggestions
    }