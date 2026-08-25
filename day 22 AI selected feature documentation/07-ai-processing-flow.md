# AI Processing Flow

## Processing Steps

1. Receive the expense description.
2. Validate the input.
3. Prepare the text for processing.
4. Transform the text using TF-IDF.
5. Pass the numerical features to Logistic Regression.
6. Predict the most suitable expense category.
7. Obtain prediction probability/confidence using `predict_proba()` where implemented.
8. Return the result as JSON.

## Processing Architecture

```text
Expense Description
        ↓
Input Validation
        ↓
Text Processing
        ↓
TF-IDF Vectorizer
        ↓
Numerical Features
        ↓
Logistic Regression
        ↓
Predicted Category
        ↓
Confidence Score
        ↓
JSON Response
```

## Example

Input: `I filled petrol in my car`

Processing:

`Text → TF-IDF → Logistic Regression → Transportation`

Output:

```json
{
  "expense": "I filled petrol in my car",
  "category": "Transportation",
  "confidence": 0.XX
}
```

## Model Files

Example:

```text
model/
├── expense_model.pkl
└── tfidf_vectorizer.pkl
```
