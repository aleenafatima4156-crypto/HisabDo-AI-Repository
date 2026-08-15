import joblib


# =========================================================
# Configuration
# =========================================================

CONFIDENCE_THRESHOLD = 0.40


# =========================================================
# Load Model and Vectorizer
# =========================================================

model = joblib.load("expense_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# =========================================================
# AI Expense Categorization Service
# =========================================================

def categorize_expense(expense):
    """
    Takes an expense description and returns
    category and confidence.
    """

    # -----------------------------
    # Input Validation
    # -----------------------------

    if not isinstance(expense, str):
        raise ValueError("Expense must be a string")

    expense = expense.strip()

    if not expense:
        raise ValueError("Expense description cannot be empty")

    if len(expense) > 200:
        raise ValueError(
            "Expense description is too long. "
            "Maximum 200 characters allowed"
        )

    # -----------------------------
    # TF-IDF Processing
    # -----------------------------

    expense_vector = vectorizer.transform([expense])

    # -----------------------------
    # ML Prediction
    # -----------------------------

    prediction = model.predict(expense_vector)[0]

    probabilities = model.predict_proba(expense_vector)[0]

    confidence = float(max(probabilities))

    # -----------------------------
    # Low Confidence Handling
    # -----------------------------

    if confidence < CONFIDENCE_THRESHOLD:
        category = "Uncategorized"
    else:
        category = prediction

    # -----------------------------
    # Return AI Result
    # -----------------------------

    return {
        "category": category,
        "confidence": round(confidence, 4)
    }