# Day 11 – Sample Inputs and Outputs

## 1. Successful Expense Categorization

### Input

```json
{
    "user_id": "U001",
    "expense": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-11"
}

### Expected Outputs

{
    "status": "success",
    "user_id": "U001",
    "description": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-11",
    "category": "Food & Groceries",
    "confidence": "ACTUAL_VALUE"
}
# 2-Bill Categorization
### Input
{
    "user_id": "U002",
    "expense": "I paid my electricity bill",
    "amount": 4500,
    "currency": "PKR",
    "date": "2026-08-11"
}

### Expected Outputs
{
    "status": "success",
    "user_id": "U002",
    "description": "I paid my electricity bill",
    "amount": 4500,
    "currency": "PKR",
    "date": "2026-08-11",
    "category": "Bills",
    "confidence": "ACTUAL_VALUE"
}

# 3. Transport Expense
### Input
{
    "user_id": "U003",
    "expense": "Spent 1500 on petrol",
    "amount": 1500,
    "currency": "PKR",
    "date": "2026-08-11"
}

### Expected Outputs

{
    "status": "success",
    "user_id": "U003",
    "description": "Spent 1500 on petrol",
    "amount": 1500,
    "currency": "PKR",
    "date": "2026-08-11",
    "category": "Transport",
    "confidence": "ACTUAL_VALUE"
}
# Invalid Input Testing

# 4. Missing Expense
### Input
{
    "user_id": "U004",
    "amount": 2000,
    "currency": "PKR",
    "date": "2026-08-11"
}

### Expected Output
{
    "status": "error",
    "message": "Expense description is required"
}
# 5. Empty Expense
### Input
{
    "user_id": "U005",
    "expense": "",
    "amount": 2000,
    "currency": "PKR",
    "date": "2026-08-11"
}
### Expected Output
{
    "status": "error",
    "message": "Expense description cannot be empty"
}