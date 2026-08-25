def automate_support(data):

    query = data.get("query", "").strip().lower()

    if not query:
        return {
            "status": "error",
            "message": "Support query is required."
        }

    # --------------------------------
    # Expense Support
    # --------------------------------

    if (
        "expense not saved" in query
        or "cannot save expense" in query
        or "expense error" in query
    ):

        return {
            "status": "success",
            "support_type": "Expense Issue",
            "automation_available": True,
            "priority": "MEDIUM",
            "automated_action": (
                "Check the expense description, amount and "
                "category, then try saving the expense again."
            ),
            "next_action": "retry"
        }

    # --------------------------------
    # Payment Support
    # --------------------------------

    elif (
        "payment failed" in query
        or "payment problem" in query
        or "payment error" in query
    ):

        return {
            "status": "success",
            "support_type": "Payment Issue",
            "automation_available": True,
            "priority": "HIGH",
            "automated_action": (
                "Check the payment information and try the "
                "transaction again."
            ),
            "next_action": "retry"
        }

    # --------------------------------
    # Login Support
    # --------------------------------

    elif (
        "cannot login" in query
        or "login failed" in query
        or "login problem" in query
    ):

        return {
            "status": "success",
            "support_type": "Login Issue",
            "automation_available": True,
            "priority": "MEDIUM",
            "automated_action": (
                "Check your email and password and try "
                "logging in again."
            ),
            "next_action": "retry_login"
        }

    # --------------------------------
    # Feature Guidance
    # --------------------------------

    elif (
        "where is" in query
        or "how do i use" in query
        or "how can i use" in query
    ):

        return {
            "status": "success",
            "support_type": "Feature Guidance",
            "automation_available": True,
            "priority": "LOW",
            "automated_action": (
                "Provide the user with feature location "
                "and usage instructions."
            ),
            "next_action": "show_feature_guidance"
        }

    # --------------------------------
    # General Help
    # --------------------------------

    elif (
        "help" in query
        or "how to" in query
        or "guide me" in query
    ):

        return {
            "status": "success",
            "support_type": "General Help",
            "automation_available": True,
            "priority": "LOW",
            "automated_action": (
                "Search the support knowledge base and "
                "provide relevant help information."
            ),
            "next_action": "search_help_articles"
        }

    # --------------------------------
    # Unknown / Complex Request
    # --------------------------------

    else:

        return {
            "status": "success",
            "support_type": "Unknown Issue",
            "automation_available": False,
            "priority": "MEDIUM",
            "automated_action": (
                "The request requires further investigation."
            ),
            "next_action": "escalate_to_human"
        }