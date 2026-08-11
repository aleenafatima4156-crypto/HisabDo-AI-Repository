from flask import Flask, request, jsonify
import joblib

# ==========================================
# Flask Application
# ==========================================

app = Flask(__name__)

# ==========================================
# Load ML Model and TF-IDF Vectorizer
# ==========================================

model = joblib.load("expense_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# ==========================================
# Home Route
# ==========================================

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "HisabDo Smart Expense Categorization API is running"
    })


# ==========================================
# Categorize Expense
# ==========================================

@app.route("/categorize", methods=["POST"])
def categorize():

    # --------------------------------------
    # 1. Check JSON input
    # --------------------------------------

    if not request.is_json:
        return jsonify({
            "status": "error",
            "message": "Request must contain JSON data"
        }), 400

    data = request.get_json()

    # --------------------------------------
    # 2. Check expense field
    # --------------------------------------

    if "expense" not in data:
        return jsonify({
            "status": "error",
            "message": "Expense description is required"
        }), 400

    expense = data["expense"]

    # --------------------------------------
    # 3. Validate expense type
    # --------------------------------------

    if not isinstance(expense, str):
        return jsonify({
            "status": "error",
            "message": "Expense must be a string"
        }), 400

    # --------------------------------------
    # 4. Check empty input
    # --------------------------------------

    if not expense.strip():
        return jsonify({
            "status": "error",
            "message": "Expense description cannot be empty"
        }), 400

    # --------------------------------------
    # 5. Check maximum length
    # --------------------------------------

    if len(expense) > 200:
        return jsonify({
            "status": "error",
            "message": "Expense description is too long. Maximum 200 characters allowed"
        }), 400

    # --------------------------------------
    # 6. Optional application fields
    # --------------------------------------

    user_id = data.get("user_id", "Unknown")
    amount = data.get("amount", None)
    currency = data.get("currency", "PKR")
    date = data.get("date", None)

    # --------------------------------------
    # 7. Convert expense into TF-IDF
    # --------------------------------------

    expense_vector = vectorizer.transform([expense])

    # --------------------------------------
    # 8. Predict category
    # --------------------------------------

    prediction = model.predict(expense_vector)[0]

    # --------------------------------------
    # 9. Calculate confidence
    # --------------------------------------

    probabilities = model.predict_proba(expense_vector)[0]

    confidence = float(max(probabilities))

    # --------------------------------------
    # 10. Low-confidence handling
    # --------------------------------------

    confidence_threshold = 0.45

    if confidence < confidence_threshold:
        category = "Uncategorized"
    else:
        category = prediction

    # --------------------------------------
    # 11. Create response
    # --------------------------------------

    response = {
        "status": "success",
        "user_id": user_id,
        "description": expense,
        "amount": amount,
        "currency": currency,
        "date": date,
        "category": category,
        "confidence": round(confidence, 4)
    }

    # --------------------------------------
    # 12. Return JSON response
    # --------------------------------------

    return jsonify(response)


# ==========================================
# Run Flask Server
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)