def track_financial_goal(data):

    required_fields = [
        "goal_name",
        "target_amount",
        "current_amount"
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

    except (ValueError, TypeError):

        return {
            "status": "error",
            "message": (
                "Target amount and current amount "
                "must be valid numbers."
            )
        }

    # Validate amounts
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

    # Calculate remaining amount
    remaining_amount = max(
        target_amount - current_amount,
        0
    )

    # Calculate progress
    progress = (
        current_amount / target_amount
    ) * 100

    progress = min(progress, 100)

    # Determine status
    if current_amount >= target_amount:

        goal_status = "Completed"

        ai_message = (
            f"Congratulations! You have reached your "
            f"{data['goal_name']} goal."
        )

    elif progress >= 75:

        goal_status = "Almost There"

        ai_message = (
            f"You have completed {progress:.2f}% of your goal. "
            "You are very close to reaching your target."
        )

    elif progress >= 50:

        goal_status = "On Track"

        ai_message = (
            f"You have completed {progress:.2f}% of your goal. "
            "Keep maintaining your saving progress."
        )

    elif progress > 0:

        goal_status = "In Progress"

        ai_message = (
            f"You have completed {progress:.2f}% of your goal. "
            "Continue saving regularly to reach your target."
        )

    else:

        goal_status = "Not Started"

        ai_message = (
            "Your goal has not started yet. "
            "Start saving regularly to make progress."
        )

    return {
        "status": "success",
        "goal": {
            "name": data["goal_name"],
            "target_amount": round(target_amount, 2),
            "current_amount": round(current_amount, 2),
            "remaining_amount": round(
                remaining_amount,
                2
            ),
            "progress_percentage": round(
                progress,
                2
            ),
            "goal_status": goal_status
        },
        "ai_message": ai_message
    }