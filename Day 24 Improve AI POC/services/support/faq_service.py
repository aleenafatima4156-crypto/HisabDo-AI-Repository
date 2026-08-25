import json
from pathlib import Path
from difflib import SequenceMatcher

FAQ_PATH = Path(__file__).resolve().parents[2] / "data" / "faq.json"

def _load_faqs():
    with open(FAQ_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _score(query, item):
    q = query.lower()
    text = " ".join([
        item.get("question", ""),
        " ".join(item.get("keywords", []))
    ]).lower()

    ratio = SequenceMatcher(None, q, text).ratio()
    keyword_hits = sum(1 for k in item.get("keywords", []) if k.lower() in q)
    return ratio + min(keyword_hits * 0.12, 0.48)

def search_faq(query):
    items = _load_faqs()
    ranked = sorted(
        ((item, _score(query, item)) for item in items),
        key=lambda x: x[1],
        reverse=True
    )
    best, score = ranked[0]

    if score >= 0.55:
        confidence = "high" if score >= 0.85 else "medium"
        return {
            "found": True,
            "answer": best["answer"],
            "category": best["category"],
            "confidence": round(min(score, 1.0), 2),
            "confidence_level": confidence
        }

    return {
        "found": False,
        "answer": (
            "I could not find a reliable answer for this question. "
            "Please rephrase your question or contact human support."
        ),
        "category": None,
        "confidence": round(min(score, 1.0), 2),
        "confidence_level": "low"
    }
