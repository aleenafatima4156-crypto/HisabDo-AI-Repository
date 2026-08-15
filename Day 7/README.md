# HisabDo – Day 7 ML Prediction API

## Student Performance Prediction

### Track
AI / ML

### Objective

The objective of this project is to deploy a trained Student Performance
Machine Learning model as a REST API using Flask.

The API accepts student performance information and returns a predicted
result along with the model confidence.

---

## 1. Features

The API provides:

- Trained ML model loading
- Student performance prediction
- REST API endpoint
- JSON request handling
- Input validation
- Missing field validation
- Numeric input validation
- Score range validation
- Prediction confidence
- JSON error responses
- API testing using Postman/Thunder Client

---

## 2. Input Features

The model accepts:

| Feature | Description | Valid Range |
|---------|-------------|-------------|
| Attendance | Student attendance score | 0–100 |
| Assignment | Assignment score | 0–100 |
| Midterm | Midterm score | 0–100 |
| Final | Final exam score | 0–100 |

---

## 3. Technology Stack

- Python
- Flask
- Scikit-learn
- Joblib
- Pandas
- NumPy
- Postman / Thunder Client

---

## 4. Project Structure

Day7/

├── app.py

├── train_model.py

├── student_model.pkl

├── requirements.txt

├── README.md

├── .gitignore

└── screenshots/

    ├── success_prediction.png
    ├── missing_field.png
    ├── invalid_score.png
    └── invalid_type.png

---

## 5. Installation

Create and activate a virtual environment:

```bash
python -m venv venv