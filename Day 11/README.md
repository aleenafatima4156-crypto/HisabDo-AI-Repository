# HisabDo – Smart Expense Categorization

## Day 11 – AI/ML Capstone

### Project Overview

HisabDo Smart Expense Categorization is an AI/ML feature that automatically categorizes user expenses from their descriptions.

The system uses a trained Machine Learning model with TF-IDF text feature extraction and Logistic Regression classification. A Flask REST API connects the ML model with the application.

---

## Objective

The objective of Day 11 is to improve the Day 10 AI prototype so that it can handle realistic application-style expense data, validate input, process ML predictions, return confidence scores, and provide structured responses to the application.

---

## AI Feature

**Smart Expense Categorization**

The system receives an expense description and predicts its appropriate financial category.

Example:

Input:

"I paid my electricity bill"

Output:

"Category: Bills"

---

## Technology Stack

- Python
- Flask
- Scikit-learn
- Pandas
- Joblib
- TF-IDF
- Logistic Regression
- REST API
- JSON
- Thunder Client

---

## Machine Learning Workflow

Application Input
↓
Flask REST API
↓
Input Validation
↓
TF-IDF Vectorization
↓
Logistic Regression
↓
Category Prediction
↓
Confidence Calculation
↓
Response Validation
↓
JSON Response
↓
Application

---

## Input Data Structure

The application sends JSON data containing:

- user_id
- expense
- amount
- currency
- date

Example:

```json
{
    "user_id": "U001",
    "expense": "I paid 4500 for electricity bill",
    "amount": 4500,
    "currency": "PKR",
    "date": "2026-08-11"
}