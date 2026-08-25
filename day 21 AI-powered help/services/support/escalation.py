def escalate_to_human(data):

    query = data.get("query", "").strip()
    issue_type = data.get("issue_type", "").strip()
    user_id = data.get("user_id", "").strip()

    if not query:
        return {
            "status": "error",
            "message": "Support query is required."
        }

    # --------------------------------
    # Determine priority
    # --------------------------------

    query_lower = query.lower()

    if (
        "payment failed" in query_lower
        or "payment issue" in query_lower
        or "transaction problem" in query_lower
    ):
        priority = "HIGH"

    elif (
        "account" in query_lower
        or "login" in query_lower
        or "cannot access" in query_lower
    ):
        priority = "HIGH"

    else:
        priority = "MEDIUM"

    # --------------------------------
    # Create support ticket
    # --------------------------------

    ticket_id = "SUP-" + str(abs(hash(query)) % 100000)

    return {
        "status": "success",
        "escalated": True,

        "support_ticket": {
            "ticket_id": ticket_id,
            "user_id": user_id if user_id else "anonymous",
            "issue_type": issue_type if issue_type else "General Support",
            "priority": priority,
            "query": query,
            "status": "Pending Human Review"
        },

        "message": (
            "Your issue has been forwarded to human support. "
            "A support representative can review the request."
        )
    }