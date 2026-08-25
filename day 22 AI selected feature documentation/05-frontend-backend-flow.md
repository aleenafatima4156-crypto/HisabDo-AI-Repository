# Frontend & Backend Flow

## Frontend Flow

1. User opens the HisabDo website or mobile application.
2. User enters an expense description.
3. The frontend sends the description to the backend API.
4. The frontend receives the prediction response.
5. Category and confidence score are displayed to the user.

## Backend Flow

1. Flask API receives the request.
2. Input is validated.
3. Expense description is transformed using TF-IDF.
4. TF-IDF features are passed to Logistic Regression.
5. The model predicts the category.
6. `predict_proba()` can provide the confidence/probability.
7. Flask returns a JSON response.

## Complete Flow

```text
User
 ↓
Enter Expense
 ↓
HisabDo Frontend
 ↓
POST /predict
 ↓
Flask API
 ↓
Input Validation
 ↓
TF-IDF Transformation
 ↓
Logistic Regression
 ↓
Category + Confidence
 ↓
JSON Response
 ↓
Frontend
```

> Keep the endpoint name consistent with the actual Flask implementation.
