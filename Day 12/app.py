from flask import Flask, request, jsonify
import joblib
import os
import time

app = Flask(__name__)

# ==========================================
# Configuration
# ==========================================

MAX_EXPENSE_LENGTH = 200
CONFIDENCE_THRESHOLD = 0.40

# ==========================================
# Load ML Model and TF-IDF Vectorizer
# ==========================================

try:
    model = joblib.load("expense_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")

    print("ML model loaded successfully!")
    print("TF-IDF vectorizer loaded successfully!")

except Exception as e:
    print("Error loading model:", e)
    model = None
    vectorizer = None


# ==========================================
# Health Check
# ==========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "success",
        "service": "HisabDo Smart Expense Categorization API",
        "version": "Day 12",
        "endpoint": "/categorize"
    })


# ==========================================
# Categorization API
# ==========================================

@app.route("/categorize", methods=["POST"])
def categorize():

    start_time = time.time()

    # --------------------------------------
    # Check JSON request
    # --------------------------------------

    if not request.is_json:

        return jsonify({
            "status": "error",
            "message": "Request must contain JSON data"
        }), 400


    data = request.get_json()


    # --------------------------------------
    # Validate request structure
    # --------------------------------------

    if not isinstance(data, dict):

        return jsonify({
            "status": "error",
            "message": "Invalid request structure"
        }), 400


    # --------------------------------------
    # Required field
    # --------------------------------------

    expense = data.get("expense")


    if expense is None:

        return jsonify({
            "status": "error",
            "message": "Expense description is required"
        }), 400


    # --------------------------------------
    # Validate expense type
    # --------------------------------------

    if not isinstance(expense, str):

        return jsonify({
            "status": "error",
            "message": "Expense must be a string"
        }), 400


    # --------------------------------------
    # Remove extra spaces
    # --------------------------------------

    expense = expense.strip()


    # --------------------------------------
    # Empty input validation
    # --------------------------------------

    if not expense:

        return jsonify({
            "status": "error",
            "message": "Expense description cannot be empty"
        }), 400


    # --------------------------------------
    # Maximum length validation
    # --------------------------------------

    if len(expense) > MAX_EXPENSE_LENGTH:

        return jsonify({
            "status": "error",
            "message": (
                f"Expense description is too long. "
                f"Maximum {MAX_EXPENSE_LENGTH} characters allowed"
            )
        }), 400


    # --------------------------------------
    # Check ML model
    # --------------------------------------

    if model is None or vectorizer is None:

        return jsonify({
            "status": "error",
            "message": "AI model is currently unavailable"
        }), 503


    # --------------------------------------
    # Convert expense text into TF-IDF
    # --------------------------------------

    try:

        expense_vector = vectorizer.transform([expense])

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": "Unable to process expense description"
        }), 500


    # --------------------------------------
    # ML Prediction
    # --------------------------------------

    try:

        prediction = model.predict(expense_vector)[0]

        probabilities = model.predict_proba(expense_vector)[0]

        confidence = float(max(probabilities))

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": "AI prediction failed"
        }), 500


    # --------------------------------------
    # Low Confidence Handling
    # --------------------------------------

    if confidence < CONFIDENCE_THRESHOLD:

        category = "Uncategorized"

    else:

        category = prediction


    # --------------------------------------
    # Response Processing
    # --------------------------------------

    processing_time = round(
        time.time() - start_time,
        4
    )


    response_data = {

        "status": "success",

        "user_id": data.get("user_id"),

        "description": expense,

        "amount": data.get("amount"),

        "currency": data.get("currency"),

        "date": data.get("date"),

        "category": category,

        "confidence": round(confidence, 4),

        "processing_time_seconds": processing_time
    }


    # --------------------------------------
    # Response Validation
    # --------------------------------------

    required_response_fields = [
        "status",
        "description",
        "category",
        "confidence"
    ]


    for field in required_response_fields:

        if field not in response_data:

            return jsonify({
                "status": "error",
                "message": "Invalid AI response"
            }), 500


    # --------------------------------------
    # Return Response
    # --------------------------------------

    return jsonify(response_data), 200


# ==========================================
# Error Handler
# ==========================================

@app.errorhandler(404)
def not_found(error):

    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404


# ==========================================
# Run Flask Server
# ==========================================

if __name__ == "__main__":

    print("\n======================================")
    print("HisabDo Smart Expense AI Service")
    print("Day 12 POC")
    print("======================================")
    print("API Endpoint: POST /categorize")
    print("Confidence Threshold:", CONFIDENCE_THRESHOLD)
    print("======================================\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )