RELATED = {
    "Expenses": [
        "How can I view my expenses?",
        "How can I edit an expense?",
        "How can I delete an expense?"
    ],
    "Invoices": [
        "How can I create an invoice?",
        "How can I edit an invoice?",
        "How can I view unpaid invoices?"
    ],
    "Reports": [
        "How can I view my reports?",
        "How can I filter a report?",
        "Can I export a report?"
    ],
    "Account": [
        "How can I update my profile?",
        "How can I change my password?",
        "How can I manage my account?"
    ]
}

def get_related_questions(query, category=None):
    return RELATED.get(category, [
        "How does this feature work?",
        "Can you explain this step?",
        "How can I contact support?"
    ])[:3]
