from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)


# ==========================================
# 1. Load Trained ML Model
# ==========================================

MODEL_FILE = "expense_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"

if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError(
        "expense_model.pkl not found. "
        "Please run train_model.py first."
    )

if not os.path.exists(VECTORIZER_FILE):
    raise FileNotFoundError(
        "tfidf_vectorizer.pkl not found. "
        "Please run train_model.py first."
    )

model = joblib.load(MODEL_FILE)
vectorizer = joblib.load(VECTORIZER_FILE)

print("ML model loaded successfully!")
print("TF-IDF vectorizer loaded successfully!")


# ==========================================
# 2. Configuration
# ==========================================

CONFIDENCE_THRESHOLD = 0.45
MAX_DESCRIPTION_LENGTH = 200


# ==========================================
# 3. Home Route
# ==========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Smart Expense Categorization API is running",
        "status": "success",
        "endpoint": "POST /categorize"
    })


# ==========================================
# 4. Expense Categorization API
# ==========================================

@app.route("/categorize", methods=["POST"])
def categorize():

    # --------------------------------------
    # Check JSON
    # --------------------------------------

    if not request.is_json:

        return jsonify({
            "error": "Request must contain JSON data"
        }), 400

    data = request.get_json()

    # --------------------------------------
    # Check expense field
    # --------------------------------------

    if "expense" not in data:

        return jsonify({
            "error": "Expense description is required"
        }), 400

    expense = data["expense"]

    # --------------------------------------
    # Check input type
    # --------------------------------------

    if not isinstance(expense, str):

        return jsonify({
            "error": "Expense must be a text string"
        }), 400

    # --------------------------------------
    # Remove extra spaces
    # --------------------------------------

    expense = expense.strip()

    # --------------------------------------
    # Check empty description
    # --------------------------------------

    if not expense:

        return jsonify({
            "error": "Expense description cannot be empty"
        }), 400

    # --------------------------------------
    # Check maximum length
    # --------------------------------------

    if len(expense) > MAX_DESCRIPTION_LENGTH:

        return jsonify({
            "error": (
                "Expense description is too long. "
                "Maximum 200 characters are allowed."
            )
        }), 400

    # --------------------------------------
    # Convert text into TF-IDF
    # --------------------------------------

    expense_vector = vectorizer.transform([expense])

    # --------------------------------------
    # Predict category
    # --------------------------------------

    prediction = model.predict(expense_vector)[0]

    # --------------------------------------
    # Calculate confidence
    # --------------------------------------

    probabilities = model.predict_proba(expense_vector)[0]

    confidence = float(max(probabilities))

    confidence = round(confidence, 3)

    # --------------------------------------
    # Low confidence handling
    # --------------------------------------

    if confidence < CONFIDENCE_THRESHOLD:

        return jsonify({
            "description": expense,
            "category": "Uncategorized",
            "confidence": confidence,
            "message": (
                "Prediction confidence is too low. "
                "Please select a category manually."
            )
        })

    # --------------------------------------
    # Successful response
    # --------------------------------------

    return jsonify({
        "description": expense,
        "category": prediction,
        "confidence": confidence
    })


# ==========================================
# 5. Health Check Endpoint
# ==========================================

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "healthy",
        "model_loaded": True,
        "vectorizer_loaded": True
    })


# ==========================================
# 6. Model Information Endpoint
# ==========================================

@app.route("/model-info", methods=["GET"])
def model_info():

    return jsonify({
        "model": "Logistic Regression",
        "feature_extraction": "TF-IDF",
        "categories": model.classes_.tolist(),
        "confidence_threshold": CONFIDENCE_THRESHOLD
    })


# ==========================================
# 7. Run Flask Application
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )