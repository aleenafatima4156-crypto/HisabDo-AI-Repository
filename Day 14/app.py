from flask import Flask, request, jsonify
from ai_service import categorize_expense
import time

app = Flask(__name__)


# =========================================================
# Home / Health Check
# =========================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "success",
        "service": "HisabDo Smart Expense Categorization API",
        "version": "Day 14",
        "endpoint": "/categorize"
    })


# =========================================================
# AI Categorization API
# =========================================================

@app.route("/categorize", methods=["POST"])
def categorize():

    start_time = time.time()

    # -----------------------------------------------------
    # 1. JSON Validation
    # -----------------------------------------------------

    if not request.is_json:

        return jsonify({
            "status": "error",
            "message": "Request must contain JSON data"
        }), 400

    data = request.get_json()

    # -----------------------------------------------------
    # 2. Request Structure Validation
    # -----------------------------------------------------

    if not isinstance(data, dict):

        return jsonify({
            "status": "error",
            "message": "Invalid request structure"
        }), 400

    # -----------------------------------------------------
    # 3. Expense Field Validation
    # -----------------------------------------------------

    expense = data.get("expense")

    if expense is None:

        return jsonify({
            "status": "error",
            "message": "Expense description is required"
        }), 400

    # -----------------------------------------------------
    # 4. AI Service Processing
    # -----------------------------------------------------

    try:

        ai_result = categorize_expense(expense)

    except ValueError as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception:

        return jsonify({
            "status": "error",
            "message": "AI service failed to process the request"
        }), 500

    # -----------------------------------------------------
    # 5. Processing Time
    # -----------------------------------------------------

    processing_time = round(
        time.time() - start_time,
        4
    )

    # -----------------------------------------------------
    # 6. Create Response
    # -----------------------------------------------------

    response_data = {

        "status": "success",

        "user_id": data.get("user_id"),

        "description": expense.strip(),

        "amount": data.get("amount"),

        "currency": data.get("currency"),

        "date": data.get("date"),

        "category": ai_result["category"],

        "confidence": ai_result["confidence"],

        "processing_time_seconds": processing_time
    }

    # -----------------------------------------------------
    # 7. Response Validation
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
    # 8. Return Response
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
# Start Server
# =========================================================

if __name__ == "__main__":

    print("\n==========================================")
    print("HisabDo AI Expense Categorization")
    print("Day 14 AI Service")
    print("==========================================")
    print("Endpoint: POST /categorize")
    print("==========================================\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )