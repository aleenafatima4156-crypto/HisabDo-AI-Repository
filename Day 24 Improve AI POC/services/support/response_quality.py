def improve_response(result):
    result.setdefault("confidence_level", "low")

    if not result.get("found"):
        result["confidence_level"] = "low"
        result["answer"] = (
            "I could not find a reliable answer for your question. "
            "Please try rephrasing it or contact human support."
        )
    return result
