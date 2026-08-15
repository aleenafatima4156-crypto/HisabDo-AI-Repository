# Day 14 – End-to-End Workflow Demonstration

## Project

HisabDo – Smart Expense Categorization

## Objective

The purpose of this workflow is to demonstrate how a user's expense
description travels from the application to the AI service and returns
a validated category and confidence score.

---

## 1. Complete Workflow

User
↓
Website / Web Application / Mobile Application
↓
Backend / API Request
↓
Flask API – /categorize
↓
Input Validation
↓
AI Service – ai_service.py
↓
TF-IDF Feature Extraction
↓
Logistic Regression Model
↓
Prediction + Confidence
↓
Low Confidence Check
↓
Response Validation
↓
JSON Response
↓
Application
↓
User

---

## 2. Step-by-Step Processing

### Step 1 – User Input

The user enters an expense description in the application.

Example:

"I bought groceries for dinner"

Additional transaction information can include:

- User ID
- Amount
- Currency
- Date

---

### Step 2 – Application Request

The application sends a POST request to the AI API.

Endpoint:

POST /categorize

Example request:

{
    "user_id": "U001",
    "expense": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-14"
}

---

### Step 3 – Input Validation

The Flask API checks:

- Request contains JSON
- Request structure is valid
- Expense field exists
- Expense is a string
- Expense is not empty
- Expense length is within the allowed limit

Invalid requests are rejected with an appropriate error response.

---

### Step 4 – AI Service

After successful validation, the request is passed to:

ai_service.py

The AI service handles the ML prediction.

---

### Step 5 – TF-IDF Processing

The expense description is converted into numerical text features
using the trained TF-IDF vectorizer.

---

### Step 6 – Machine Learning Prediction

The processed text is passed to the trained Logistic Regression model.

The model predicts the most suitable expense category.

---

### Step 7 – Confidence Calculation

The model calculates prediction probabilities.

The highest probability is returned as the confidence score.

If confidence is below the configured threshold, the category is
returned as:

Uncategorized

---

### Step 8 – Response Creation

The API creates a structured JSON response containing:

- Status
- User ID
- Description
- Amount
- Currency
- Date
- Category
- Confidence
- Processing time

---

### Step 9 – Response Validation

Before returning the result, the API checks that required response
fields are available.

Required fields include:

- status
- description
- category
- confidence

---

### Step 10 – Application Response

The validated JSON response is returned to the Website, Web
Application, or Mobile Application.

---

## 3. Successful Example

### Input

{
    "user_id": "U001",
    "expense": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-14"
}

### Expected Output

{
    "status": "success",
    "user_id": "U001",
    "description": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-14",
    "category": "Food & Groceries",
    "confidence": 0.XX,
    "processing_time_seconds": 0.XX
}

Note: Confidence and processing time should be replaced with the
actual values obtained during API testing.

---

## 4. Invalid Input Example

### Input

{
    "user_id": "U002",
    "amount": 4500,
    "currency": "PKR"
}

### Output

{
    "status": "error",
    "message": "Expense description is required"
}

---

## 5. End-to-End Result

The complete workflow demonstrates that:

Application input
→ API validation
→ AI service
→ ML model
→ Prediction
→ Confidence calculation
→ Response validation
→ Application response

The POC therefore provides an application-ready foundation for
integrating Smart Expense Categorization into the HisabDo ecosystem.