# Day 14 – Application Integration

## Smart Expense Categorization

The Smart Expense Categorization AI service is designed as a REST
service that can communicate with the HisabDo application through
backend/API requests.

---

## 1. Website Integration

Website
↓
HisabDo Backend
↓
POST /categorize
↓
AI Service
↓
ML Model
↓
Category + Confidence
↓
Backend
↓
Website

The website can provide an expense input form. After submission,
the backend sends the expense description to the AI service and
returns the predicted category.

---

## 2. Web Application Integration

Web Application
↓
Backend API
↓
AI Service
↓
TF-IDF
↓
Logistic Regression
↓
Prediction + Confidence
↓
Web Application

The web application can display the predicted category before the
user saves the expense.

---

## 3. Mobile Application Integration

Mobile Application
↓
HisabDo Backend
↓
AI API
↓
ML Model
↓
JSON Response
↓
Mobile Application

The mobile application can send transaction data using a secure
HTTPS API request.

---

## 4. Example API Request

POST /categorize

{
    "user_id": "U001",
    "expense": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-14"
}

---

## 5. Example API Response

{
    "status": "success",
    "category": "Food & Groceries",
    "confidence": 0.XX
}

---

## 6. Integration Requirements

The proposed integration requires:

- Python service
- Flask REST API
- Trained ML model
- TF-IDF vectorizer
- Backend API communication
- Database for storing transactions
- Authentication and authorization
- HTTPS in production

An external AI API is not required for the current POC because the
classification model is locally hosted.

---

## 7. Production Considerations

Before production deployment, the following should be added:

- HTTPS
- Authentication
- Authorization
- Rate limiting
- Secure logging
- Monitoring
- Model versioning
- Database integration
- Error monitoring
- API performance monitoring