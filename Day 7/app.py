from flask import Flask, request, jsonify
import joblib


# ==========================================
# 1. Create Flask App
# ==========================================

app = Flask(__name__)


# ==========================================
# 2. Load Trained ML Model
# ==========================================

model = joblib.load("student_model.pkl")


# ==========================================
# 3. Home / Health Check
# ==========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "success",
        "message": "Student Performance Prediction API",
        "endpoint": "POST /predict"
    })


# ==========================================
# 4. Prediction Endpoint
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    # --------------------------------------
    # Check JSON
    # --------------------------------------

    if not request.is_json:

        return jsonify({
            "status": "error",
            "message": "Request must contain JSON data"
        }), 400

    data = request.get_json()

    # --------------------------------------
    # Required Fields
    # --------------------------------------

    required_fields = [
        "Attendance",
        "Assignment",
        "Midterm",
        "Final"
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in data
    ]

    if missing_fields:

        return jsonify({
            "status": "error",
            "message": "Missing required fields",
            "missing_fields": missing_fields
        }), 400

    # --------------------------------------
    # Validate Numeric Input
    # --------------------------------------

    try:

        attendance = float(data["Attendance"])
        assignment = float(data["Assignment"])
        midterm = float(data["Midterm"])
        final = float(data["Final"])

    except (ValueError, TypeError):

        return jsonify({
            "status": "error",
            "message": "All scores must be numeric"
        }), 400

    # --------------------------------------
    # Validate Score Range
    # --------------------------------------

    scores = {
        "Attendance": attendance,
        "Assignment": assignment,
        "Midterm": midterm,
        "Final": final
    }

    invalid_scores = {
        name: value
        for name, value in scores.items()
        if value < 0 or value > 100
    }

    if invalid_scores:

        return jsonify({
            "status": "error",
            "message": "Scores must be between 0 and 100",
            "invalid_scores": invalid_scores
        }), 400

    # --------------------------------------
    # Prepare Model Input
    # --------------------------------------

    input_data = [[
        attendance,
        assignment,
        midterm,
        final
    ]]

    # --------------------------------------
    # Make Prediction
    # --------------------------------------

    prediction = model.predict(input_data)[0]

    # --------------------------------------
    # Calculate Confidence
    # --------------------------------------

    probabilities = model.predict_proba(input_data)[0]

    confidence = float(max(probabilities))

    # --------------------------------------
    # Return Response
    # --------------------------------------

    return jsonify({
        "status": "success",
        "prediction": prediction,
        "confidence": round(confidence, 4)
    }), 200


# ==========================================
# 5. 404 Error Handler
# ==========================================

@app.errorhandler(404)
def page_not_found(error):

    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404


# ==========================================
# 6. Start API
# ==========================================

if __name__ == "__main__":

    print("\n======================================")
    print("Student Performance Prediction API")
    print("======================================")
    print("Endpoint: POST /predict")
    print("======================================\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )