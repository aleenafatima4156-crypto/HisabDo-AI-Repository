import json
import os


def load_help_articles():

    file_path = os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)
            )
        ),
        "data",
        "help_articles.json"
    )

    try:

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:

        return []


def suggest_help_articles(data):

    query = data.get("query", "").strip().lower()

    if not query:

        return {
            "status": "error",
            "message": "User query is required."
        }

    articles = load_help_articles()

    if not articles:

        return {
            "status": "error",
            "message": "Help article knowledge base is unavailable."
        }

    results = []

    for article in articles:

        score = 0

        # Check title
        if query in article["title"].lower():
            score += 5

        # Check description
        if query in article["description"].lower():
            score += 2

        # Check keywords
        for keyword in article["keywords"]:

            if keyword.lower() in query:
                score += 3

            elif query in keyword.lower():
                score += 2

        if score > 0:

            results.append({
                "id": article["id"],
                "title": article["title"],
                "category": article["category"],
                "description": article["description"],
                "relevance_score": score
            })

    # Highest relevance first
    results.sort(
        key=lambda x: x["relevance_score"],
        reverse=True
    )

    # Return top 3
    results = results[:3]

    return {
        "status": "success",
        "query": query,
        "articles_found": len(results),
        "suggestions": results
    }