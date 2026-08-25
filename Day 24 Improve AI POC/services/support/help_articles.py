ARTICLES = {
    "expense": [
        {"title": "Adding an Expense", "category": "Expenses"},
        {"title": "Managing Expenses", "category": "Expenses"}
    ],
    "invoice": [
        {"title": "Creating an Invoice", "category": "Invoices"},
        {"title": "Managing Invoices", "category": "Invoices"}
    ],
    "report": [
        {"title": "Viewing Reports", "category": "Reports"}
    ]
}

def suggest_help_articles(data):
    query = str(data.get("query", "")).strip().lower()
    results = []

    for keyword, articles in ARTICLES.items():
        if keyword in query:
            results.extend(articles)

    return {
        "query": query,
        "articles": results[:5]
    }
