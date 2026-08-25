def generate_error_assistance(data):
    message = str(data.get("error_message", "")).strip()
    feature = str(data.get("feature", "the application")).strip()

    if not message:
        return {
            "feature": feature,
            "error": None,
            "suggestion": "Please provide the error message."
        }

    return {
        "feature": feature,
        "error": message,
        "suggestion": (
            "Check the required fields, verify your connection, "
            "try again, and contact support if the issue continues."
        )
    }
