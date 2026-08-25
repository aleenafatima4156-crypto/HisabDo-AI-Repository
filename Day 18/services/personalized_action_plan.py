def generate_action_plan(data):

    required_fields = [
        "goal_name",
        "target_amount",
        "current_amount",
        "monthly_income",
        "monthly_expenses"
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
        target_amount = float(data["target_amount"])
        current_amount = float(data["current_amount"])
        monthly_income = float(data["monthly_income"])
        monthly_expenses = float(data["monthly_expenses"])

    except (ValueError, TypeError):

        return {
            "status": "error",
            "message": (
                "All financial values must be valid numbers."
            )
        }

    # Validate values
    if target_amount <= 0:

        return {
            "status": "error",
            "message": "Target amount must be greater than zero."
        }

    if current_amount < 0:

        return {
            "status": "error",
            "message": "Current amount cannot be negative."
        }

    if monthly_income < 0 or monthly_expenses < 0:

        return {
            "status": "error",
            "message": "Income and expenses cannot be negative."
        }

    # --------------------------------
    # Calculations
    # --------------------------------

    remaining_amount = max(
        target_amount - current_amount,
        0
    )

    available_amount = max(
        monthly_income - monthly_expenses,
        0
    )

    progress_percentage = min(
        (current_amount / target_amount) * 100,
        100
    )

    # --------------------------------
    # Already completed
    # --------------------------------

    if remaining_amount == 0:

        return {
            "status": "success",
            "goal_name": data["goal_name"],
            "progress_percentage": 100,
            "status_label": "Completed",
            "action_plan": [
                "Goal completed successfully.",
                "Consider setting your next financial goal.",
                "Continue monitoring your spending."
            ]
        }

    # --------------------------------
    # Action plan
    # --------------------------------

    action_plan = []

    # Step 1
    action_plan.append(
        f"Remaining amount for your goal is "
        f"PKR {remaining_amount:.2f}."
    )

    # Step 2
    if available_amount > 0:

        action_plan.append(
            f"You currently have approximately "
            f"PKR {available_amount:.2f} available "
            f"after monthly expenses."
        )

    else:

        action_plan.append(
            "Your current expenses are equal to or "
            "higher than your income. Review your "
            "monthly expenses before increasing savings."
        )

    # Step 3
    if available_amount > 0:

        if available_amount >= remaining_amount:

            action_plan.append(
                "Your available monthly amount could "
                "cover the remaining goal amount."
            )

        else:

            months_needed = (
                remaining_amount / available_amount
            )

            action_plan.append(
                f"At the current saving capacity, "
                f"the goal may require approximately "
                f"{months_needed:.1f} months."
            )

    # Step 4
    action_plan.append(
        "Review your spending regularly and "
        "track your progress toward the goal."
    )

    # --------------------------------
    # AI-style recommendation
    # --------------------------------

    if available_amount <= 0:

        ai_message = (
            "Focus first on improving the gap between "
            "income and expenses before increasing "
            "your savings target."
        )

    elif available_amount < remaining_amount / 12:

        ai_message = (
            "Your current saving capacity may be low "
            "for this goal. Consider reducing avoidable "
            "expenses or extending the target timeline."
        )

    else:

        ai_message = (
            "Your goal is achievable with consistent "
            "saving and regular expense monitoring."
        )

    return {
        "status": "success",
        "goal_name": data["goal_name"],
        "target_amount": round(target_amount, 2),
        "current_amount": round(current_amount, 2),
        "remaining_amount": round(remaining_amount, 2),
        "progress_percentage": round(
            progress_percentage,
            2
        ),
        "monthly_income": round(monthly_income, 2),
        "monthly_expenses": round(monthly_expenses, 2),
        "monthly_available_amount": round(
            available_amount,
            2
        ),
        "action_plan": action_plan,
        "ai_message": ai_message
    }