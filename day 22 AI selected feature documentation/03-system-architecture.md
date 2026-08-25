# System Architecture

The system follows a client-server architecture. The HisabDo application sends an expense description to a Flask REST API. The API validates the input, processes the text using TF-IDF, and uses the trained Logistic Regression model to predict the expense category.

## Architecture Flow

```text
User
  ↓
HisabDo Website / Mobile App
  ↓
Flask REST API
  ↓
Input Validation
  ↓
TF-IDF Vectorizer
  ↓
Logistic Regression Model
  ↓
Predicted Category + Confidence Score
  ↓
JSON Response
  ↓
HisabDo Application
```

## Main Components

1. User Interface
2. HisabDo Application
3. Flask REST API
4. Input Validation
5. TF-IDF Vectorizer
6. Logistic Regression Model
7. Confidence Score
8. JSON Response

The architecture keeps the frontend, API, and machine-learning model separated for easier maintenance, testing, and integration.
