# HisabDo AI Help & Support
# Sample Inputs / Outputs

This file contains sample requests and expected API responses for the
HisabDo AI Help & Support prototype.

---

## 1. Health Check

### Input

```http
GET /health
```

### Output

```json
{
  "status": "success",
  "message": "API health check successful.",
  "data": {
    "service": "HisabDo AI Help & Support",
    "status": "healthy"
  }
}
```

---

## 2. Context-Aware Assistance

### Input

```json
{
  "current_page": "Expenses",
  "user_action": "Add Expense",
  "query": "How do I add an expense?"
}
```

### Endpoint

```http
POST /ai/help/context
```

### Output

```json
{
  "status": "success",
  "message": "Context-aware help generated.",
  "data": {
    "current_page": "Expenses",
    "user_action": "Add Expense",
    "query": "How do I add an expense?",
    "guidance": "You are currently on Expenses. For 'Add Expense', follow the instructions shown in the app or ask a more specific question for step-by-step help."
  }
}
```

---

## 3. Feature Guidance

### Input

```json
{
  "feature": "Expenses"
}
```

### Endpoint

```http
POST /ai/help/feature
```

### Output

```json
{
  "status": "success",
  "message": "Feature guidance generated.",
  "data": {
    "feature": "Expenses",
    "guidance": "Open the Expenses section, choose Add Expense, enter the details, and save."
  }
}
```

---

## 4. Step-by-Step Help

### Input

```json
{
  "task": "add expense"
}
```

### Endpoint

```http
POST /ai/help/steps
```

### Output

```json
{
  "status": "success",
  "message": "Step-by-step help generated.",
  "data": {
    "task": "add expense",
    "steps": [
      "Open the Expenses section.",
      "Select Add Expense.",
      "Enter the expense details.",
      "Review the information.",
      "Save the expense."
    ]
  }
}
```

---

## 5. Error Assistance

### Input

```json
{
  "error_message": "Unable to save expense",
  "feature": "Expenses"
}
```

### Endpoint

```http
POST /ai/help/error
```

### Output

```json
{
  "status": "success",
  "message": "Error assistance generated.",
  "data": {
    "feature": "Expenses",
    "error": "Unable to save expense",
    "suggestion": "Check the required fields, verify your connection, try again, and contact support if the issue continues."
  }
}
```

---

## 6. Help Articles

### Input

```json
{
  "query": "expense"
}
```

### Endpoint

```http
POST /ai/help/articles
```

### Output

```json
{
  "status": "success",
  "message": "Help articles suggested.",
  "data": {
    "query": "expense",
    "articles": [
      {
        "title": "Adding an Expense",
        "category": "Expenses"
      },
      {
        "title": "Managing Expenses",
        "category": "Expenses"
      }
    ]
  }
}
```

---

## 7. FAQ Support — Successful Query

### Input

```json
{
  "query": "How can I add an expense?"
}
```

### Endpoint

```http
POST /ai/help/faq
```

### Output

```json
{
  "status": "success",
  "message": "AI support response generated.",
  "data": {
    "found": true,
    "answer": "Open the Expenses section, select Add Expense, enter the expense details, review them, and save the transaction.",
    "category": "Expenses",
    "confidence": 1.0,
    "confidence_level": "high",
    "related_questions": [
      "How can I view my expenses?",
      "How can I edit an expense?",
      "How can I delete an expense?"
    ]
  }
}
```

---

## 8. Unknown Question / Safe Fallback

### Input

```json
{
  "query": "How can I become a better business owner?"
}
```

### Endpoint

```http
POST /ai/help/faq
```

### Output

```json
{
  "status": "success",
  "message": "AI support response generated.",
  "data": {
    "found": false,
    "answer": "I could not find a reliable answer for your question. Please try rephrasing it or contact human support.",
    "category": null,
    "confidence_level": "low",
    "related_questions": []
  }
}
```

**Purpose:** The system avoids generating an unsupported answer when no
reliable FAQ match is available.

---

## 9. Invalid Input

### Input

```json
{}
```

### Endpoint

```http
POST /ai/help/faq
```

### Output

```json
{
  "status": "error",
  "message": "Request data is required.",
  "data": null
}
```

**HTTP Status:** `400 Bad Request`

---

## 10. Long Query Validation

### Input

A query containing more than 500 characters.

### Output

```json
{
  "status": "error",
  "message": "Query must not exceed 500 characters.",
  "data": null
}
```

**HTTP Status:** `400 Bad Request`

---

## 11. Human Escalation

### Input

```json
{
  "user_id": "U001",
  "issue_type": "Payment Issue",
  "query": "My payment failed and I need support."
}
```

### Endpoint

```http
POST /ai/help/escalate
```

### Output

```json
{
  "status": "success",
  "message": "Support request escalated.",
  "data": {
    "escalated": true,
    "ticket_id": "HD-XXXXXXXX",
    "priority": "HIGH",
    "issue_type": "Payment Issue",
    "message": "Your issue has been prepared for human support."
  }
}
```

**Note:** The ticket ID is generated dynamically by the application.

---

## 12. Support Automation

### Input

```json
{
  "query": "I need help with my expense."
}
```

### Endpoint

```http
POST /ai/help/automate
```

### Output

```json
{
  "status": "success",
  "message": "Support request automated.",
  "data": {
    "automated": true,
    "action": "Support request classified and prepared for assistance.",
    "query": "I need help with my expense."
  }
}
```

---

## 13. Invalid Endpoint

### Input

```http
GET /wrong-endpoint
```

### Output

```json
{
  "status": "error",
  "message": "API endpoint not found.",
  "data": null
}
```

**HTTP Status:** `404 Not Found`

---

## 14. Wrong HTTP Method

### Input

```http
GET /ai/help/faq
```

### Output

```json
{
  "status": "error",
  "message": "HTTP method not allowed.",
  "data": null
}
```

**HTTP Status:** `405 Method Not Allowed`

---

## 15. Rate Limiting

The FAQ endpoint is configured with:

```text
20 requests per minute per client IP
```

When the configured limit is exceeded:

```json
{
  "status": "error",
  "message": "Too many requests. Please try again later.",
  "data": null
}
```

**HTTP Status:** `429 Too Many Requests`

---

# Testing Tools

The prototype can be tested using:

- Thunder Client
- Browser