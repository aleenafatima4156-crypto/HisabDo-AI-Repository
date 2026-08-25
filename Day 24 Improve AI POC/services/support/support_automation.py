def automate_support(data):
    query = str(data.get("query", "")).strip()

    if not query:
        return {
            "automated": False,
            "action": "No request provided."
        }

    return {
        "automated": True,
        "action": "Support request classified and prepared for assistance.",
        "query": query
    }
