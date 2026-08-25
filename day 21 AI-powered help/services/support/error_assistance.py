def generate_error_assistance(data):

    error_message = data.get("error", "").strip().lower()
    page = data.get("page", "").strip().lower()

    if not error_message:

        return {
            "status": "error",
            "message": "Error message is required."
        }

    # --------------------------------
    # Payment errors
    # --------------------------------

    if (
        "payment failed" in error_message
        or "payment error" in error_message
    ):

        error_type = "Payment Error"

        reason = (
            "The payment could not be completed. "
            "The payment details may be incomplete "
            "or the transaction may have failed."
        )

        solution = (
            "Check the payment information and try again. "
            "If the problem continues, contact support."
        )

        severity = "HIGH"

    # --------------------------------
    # Invalid amount
    # --------------------------------

    elif (
        "invalid amount" in error_message
        or "amount is invalid" in error_message
    ):

        error_type = "Invalid Amount"

        reason = (
            "The entered amount is missing, invalid "
            "or not in the expected numeric format."
        )

        solution = (
            "Enter a valid positive number for the amount "
            "and try again."
        )

        severity = "MEDIUM"

    # --------------------------------
    # Expense save error
    # --------------------------------

    elif (
        "expense not saved" in error_message
        or "expense save" in error_message
    ):

        error_type = "Expense Save Error"

        reason = (
            "The expense could not be saved. "
            "Some required information may be missing."
        )

        solution = (
            "Check the expense description, amount and category, "
            "then try saving the expense again."
        )

        severity = "MEDIUM"

    # --------------------------------
    # Authentication error
    # --------------------------------

    elif (
        "invalid login" in error_message
        or "login failed" in error_message
    ):

        error_type = "Login Error"

        reason = (
            "The login information could not be verified."
        )

        solution = (
            "Check your email and password and try again."
        )

        severity = "MEDIUM"

    # --------------------------------
    # Network error
    # --------------------------------

    elif (
        "network error" in error_message
        or "connection error" in error_message
        or "server unavailable" in error_message
    ):

        error_type = "Connection Error"

        reason = (
            "The application could not communicate "
            "with the server."
        )

        solution = (
            "Check your internet connection and try again "
            "after a short while."
        )

        severity = "HIGH"

    # --------------------------------
    # Unknown error
    # --------------------------------

    else:

        error_type = "Unknown Error"

        reason = (
            "The system could not identify the exact cause "
            "of this error."
        )

        solution = (
            "Try the action again. If the problem continues, "
            "provide the error message to support."
        )

        severity = "MEDIUM"

    return {
        "status": "success",

        "error_analysis": {
            "error_type": error_type,
            "severity": severity,
            "original_error": error_message,
            "page": page
        },

        "possible_reason": reason,

        "recommended_action": solution
    }