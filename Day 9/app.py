from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Training data
expenses = [
    "pizza burger food",
    "restaurant dinner lunch",
    "grocery vegetables milk",
    "uber taxi bus",
    "petrol fuel transport",
    "clothes shoes shopping",
    "online shopping bags",
    "electricity gas bill",
    "internet phone bill",
    "movie cinema",
    "games entertainment",
    "books school education"
]

categories = [
    "Food & Groceries",
    "Food & Groceries",
    "Food & Groceries",
    "Transport",
    "Transport",
    "Shopping",
    "Shopping",
    "Bills",
    "Bills",
    "Entertainment",
    "Entertainment",
    "Education"
]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(expenses)

# Train ML model
model = LogisticRegression()
model.fit(X, categories)


@app.route("/")
def home():
    return "Smart Expense Categorization API is Running!"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    expense = data.get("expense")

    if not expense:
        return jsonify({
            "error": "Expense description is required"
        }), 400

    # Convert input into TF-IDF features
    X_test = vectorizer.transform([expense])

    # Predict category
    prediction = model.predict(X_test)[0]

    return jsonify({
        "expense": expense,
        "category": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)