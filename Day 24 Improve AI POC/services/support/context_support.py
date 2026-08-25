def generate_context_help(data):
    page = data.get("current_page", "the current page")
    action = data.get("user_action", "your current action")
    query = data.get("query", "your request")

    return {
        "current_page": page,
        "user_action": action,
        "query": query,
        "guidance": (
            f"You are currently on {page}. "
            f"For '{action}', follow the instructions shown in the app "
            "or ask a more specific question for step-by-step help."
        )
    }
