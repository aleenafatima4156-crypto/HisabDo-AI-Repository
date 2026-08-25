import uuid

def escalate_to_human(data):
    ticket_id = "HD-" + uuid.uuid4().hex[:8].upper()

    return {
        "escalated": True,
        "ticket_id": ticket_id,
        "priority": "HIGH",
        "issue_type": data.get("issue_type", "General Support"),
        "message": "Your issue has been prepared for human support."
    }
