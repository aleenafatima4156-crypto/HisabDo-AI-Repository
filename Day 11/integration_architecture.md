# Day 11 – Integration Architecture

## Smart Expense Categorization

The Smart Expense Categorization feature uses a Flask REST API to connect the application with the trained machine learning model.

## Architecture Flow

Application
    ↓
Website / Web Application / Mobile Application
    ↓
Flask REST API
    ↓
Input Validation
    ↓
AI/ML Service
    ↓
TF-IDF Vectorizer
    ↓
Logistic Regression Model
    ↓
Category + Confidence
    ↓
Response Validation
    ↓
JSON Response
    ↓
Website / Web Application / Mobile Application


## Component Explanation

### 1. Application Layer

The feature can be integrated into:

- HisabDo Website
- HisabDo Web Application
- HisabDo Mobile Application

The user enters an expense description along with transaction information.

### 2. Backend/API Layer

The Flask REST API receives the application request through:

POST /categorize

The API validates the received data before sending the expense description to the ML model.

### 3. Input Validation

The API checks:

- JSON request format
- Expense field availability
- Expense data type
- Empty descriptions
- Maximum description length

Invalid requests receive an appropriate error response.

### 4. AI/ML Service

The validated expense description is processed by the trained machine learning pipeline.

The pipeline contains:

- TF-IDF Vectorizer
- Logistic Regression Classifier

### 5. Prediction Layer

The Logistic Regression model predicts the most suitable expense category.

The model also provides class probabilities that are used to calculate the confidence score.

### 6. Response Layer

The API returns a JSON response containing:

- User ID
- Expense description
- Amount
- Currency
- Date
- Predicted category
- Confidence score
- Status

### Example Response

{
    "status": "success",
    "user_id": "U001",
    "description": "I paid my electricity bill",
    "amount": 4500,
    "currency": "PKR",
    "date": "2026-08-11",
    "category": "Bills",
    "confidence": 0.XX
}

## Technology Requirements

| Component | Technology |
|---|---|
| Application | Website / Web App / Mobile App |
| Backend | Flask |
| API | REST API |
| Programming Language | Python |
| Text Processing | TF-IDF |
| ML Model | Logistic Regression |
| Model Storage | Joblib |
| Data Format | JSON / CSV |
| External AI API | Not required |
| Prompt Engineering | Not required |
| Database | Future integration |
| Background Processing | Not required for current POC |

## Future Integration

In a production version, the API can be connected to a database to store:

- User accounts
- Expense transactions
- Predicted categories
- Confidence scores
- Historical financial records

The model can also be periodically retrained using new verified expense categories.