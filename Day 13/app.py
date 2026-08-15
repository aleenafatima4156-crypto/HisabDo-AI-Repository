from flask import Flask, request, jsonify
import joblib
import time

app = Flask(__name__)

# =========================================================
# Configuration
# =========================================================

MAX_EXPENSE_LENGTH = 200
CONFIDENCE_THRESHOLD = 0.40


# =========================================================
# Load ML Model and TF-IDF Vectorizer
# =========================================================

try:
    model = joblib.load("expense_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")

    print("ML model loaded successfully!")
    print("TF-IDF vectorizer loaded successfully!")

except Exception as e:
    print("Error loading model:", e)

    model = None
    vectorizer = None


# =========================================================
# Home / Health Check
# =========================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "success",
        "service": "HisabDo Smart Expense Categorization API",
        "version": "Day 13",
        "endpoint": "/categorize"
    })


# =========================================================
# Smart Expense Categorization
# =========================================================

@app.route("/categorize", methods=["POST"])
def categorize():

    start_time = time.time()

    # -----------------------------------------------------
    # 1. Check JSON
    # -----------------------------------------------------

    if not request.is_json:

        return jsonify({
            "status": "error",
            "message": "Request must contain JSON data"
        }), 400


    data = request.get_json()


    # -----------------------------------------------------
    # 2. Validate Request Structure
    # -----------------------------------------------------

    if not isinstance(data, dict):

        return jsonify({
            "status": "error",
            "message": "Invalid request structure"
        }), 400


    # -----------------------------------------------------
    # 3. Get Expense Description
    # -----------------------------------------------------

    expense = data.get("expense")


    if expense is None:

        return jsonify({
            "status": "error",
            "message": "Expense description is required"
        }), 400


    # -----------------------------------------------------
    # 4. Validate Expense Type
    # -----------------------------------------------------

    if not isinstance(expense, str):

        return jsonify({
            "status": "error",
            "message": "Expense must be a string"
        }), 400


    # -----------------------------------------------------
    # 5. Remove Extra Spaces
    # -----------------------------------------------------

    expense = expense.strip()


    # -----------------------------------------------------
    # 6. Empty Input Validation
    # -----------------------------------------------------

    if not expense:

        return jsonify({
            "status": "error",
            "message": "Expense description cannot be empty"
        }), 400


    # -----------------------------------------------------
    # 7. Very Long Input Validation
    # -----------------------------------------------------

    if len(expense) > MAX_EXPENSE_LENGTH:

        return jsonify({
            "status": "error",
            "message": (
                f"Expense description is too long. "
                f"Maximum {MAX_EXPENSE_LENGTH} characters allowed"
            )
        }), 400


    # -----------------------------------------------------
    # 8. Check Model Availability
    # -----------------------------------------------------

    if model is None or vectorizer is None:

        return jsonify({
            "status": "error",
            "message": "AI model is currently unavailable"
        }), 503


    # -----------------------------------------------------
    # 9. TF-IDF Processing
    # -----------------------------------------------------

    try:

        expense_vector = vectorizer.transform([expense])

    except Exception:

        return jsonify({
            "status": "error",
            "message": "Unable to process expense description"
        }), 500


    # -----------------------------------------------------
    # 10. ML Prediction
    # -----------------------------------------------------

    try:

        prediction = model.predict(expense_vector)[0]

        probabilities = model.predict_proba(expense_vector)[0]

        confidence = float(max(probabilities))

    except Exception:

        return jsonify({
            "status": "error",
            "message": "AI prediction failed"
        }), 500


    # -----------------------------------------------------
    # 11. Low Confidence Handling
    # -----------------------------------------------------

    if confidence < CONFIDENCE_THRESHOLD:

        category = "Uncategorized"

    else:

        category = prediction


    # -----------------------------------------------------
    # 12. Calculate Processing Time
    # -----------------------------------------------------

    processing_time = round(
        time.time() - start_time,
        4
    )


    # -----------------------------------------------------
    # 13. Create Response
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # 14. Response Validation
    # -----------------------------------------------------

    required_fields = [
        "status",
        "description",
        "category",
        "confidence"
    ]


    for field in required_fields:

        if field not in response_data:

            return jsonify({
                "status": "error",
                "message": "Invalid AI response"
            }), 500


    # -----------------------------------------------------
    # 15. Return Final Response
    # -----------------------------------------------------

    return jsonify(response_data), 200


# =========================================================
# 404 Error Handler
# =========================================================

@app.errorhandler(404)
def not_found(error):

    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404


# =========================================================
# Start Flask Server
# =========================================================

if __name__ == "__main__":

    print("\n==============================================")
    print("HisabDo Smart Expense Categorization API")
    print("Day 13 AI/ML POC")
    print("==============================================")
    print("Endpoint: POST /categorize")
    print("Confidence Threshold:", CONFIDENCE_THRESHOLD)
    print("==============================================\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )