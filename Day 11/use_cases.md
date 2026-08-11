# Day 11 – Smart Expense Categorization
## Realistic AI/ML Use Cases

### Use Case 1 – Automatic Expense Categorization

#### Problem
Users often have to manually select a category every time they record an expense. This can be time-consuming and users may select the wrong category.

#### AI Solution
The Smart Expense Categorization model automatically predicts the appropriate category from the expense description.

#### Application Input

{
    "user_id": "U001",
    "expense": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-11"
}

#### Expected Output

{
    "status": "success",
    "user_id": "U001",
    "description": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-11",
    "category": "Food & Groceries",
    "confidence": 0.XX
}

#### Benefit
The feature saves user time and makes expense records more organized.


---

### Use Case 2 – Automatic Bill Classification

#### Problem
Users record different types of bills such as electricity, internet, water, and mobile bills. Manually categorizing every bill can be inconvenient.

#### AI Solution
The AI model analyzes the expense description and automatically identifies bill-related expenses.

#### Application Input

{
    "user_id": "U002",
    "expense": "I paid my electricity bill",
    "amount": 4500,
    "currency": "PKR",
    "date": "2026-08-11"
}

#### Expected Output

{
    "status": "success",
    "user_id": "U002",
    "description": "I paid my electricity bill",
    "amount": 4500,
    "currency": "PKR",
    "date": "2026-08-11",
    "category": "Bills",
    "confidence": 0.XX
}

#### Benefit
Bills can be automatically organized, making monthly financial tracking easier.


---

### Use Case 3 – Mobile Expense Entry

#### Problem
Mobile users frequently record expenses while travelling, shopping, eating out, or purchasing fuel. They need a quick way to record transactions without manually selecting categories.

#### AI Solution
The mobile application sends the expense description to the Flask AI API. The ML model predicts the category and sends the result back to the mobile application.

#### Application Input

{
    "user_id": "U003",
    "expense": "Spent 1500 on petrol",
    "amount": 1500,
    "currency": "PKR",
    "date": "2026-08-11"
}

#### Expected Output

{
    "status": "success",
    "user_id": "U003",
    "description": "Spent 1500 on petrol",
    "amount": 1500,
    "currency": "PKR",
    "date": "2026-08-11",
    "category": "Transport",
    "confidence": 0.XX
}

#### Benefit
Users can record expenses faster while the application automatically organizes the transaction.


---

## AI/ML Technology Used

- Python
- Flask REST API
- TF-IDF Vectorization
- Logistic Regression
- Joblib
- JSON-based API communication

## Current POC Architecture

Application
↓
Flask Backend/API
↓
Input Validation
↓
TF-IDF Vectorizer
↓
Logistic Regression Model
↓
Prediction + Confidence
↓
JSON Response
↓
Application

## Integration

The Website, Web Application, and Mobile Application can communicate with the Smart Expense Categorization service through the Flask REST API.

The current solution uses a locally trained ML model and does not require an external AI API or prompt engineering.

A database can be added in a future production version to store users, transactions, categories, and prediction results.