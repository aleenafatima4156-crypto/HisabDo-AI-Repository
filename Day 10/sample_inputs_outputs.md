# Day 10 – Sample Inputs and Outputs

## Project

HisabDo – Smart Expense Categorization

## AI Feature

Smart Expense Categorization

The system accepts a natural-language expense description and automatically predicts
the most appropriate expense category using a machine learning model.

---

# 1. Successful Prediction – Food & Groceries

### Input

```json
{
    "expense": "I paid for petrol"
}

### Output

{
  "category": "Transport",
  "confidence": 0.507,
  "description": "I paid for petrol"
}