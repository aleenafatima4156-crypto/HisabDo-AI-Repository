# Testing Scenarios & Results

## Testing Approach

The API should be tested with valid, invalid, empty, missing, and unfamiliar inputs to verify prediction, confidence output, validation, and error handling.

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| TC-01 | Bought groceries | Food & Groceries |
| TC-02 | Paid electricity bill | Bills & Utilities |
| TC-03 | Filled petrol in car | Transportation |
| TC-04 | Bought new shoes | Shopping |
| TC-05 | Paid university fee | Education |
| TC-06 | Empty expense | Validation error |
| TC-07 | Missing `expense` field | Validation error |
| TC-08 | Unfamiliar expense | Category + confidence |

## Valid Input Example

```json
{
  "expense": "Bought groceries"
}
```

Expected response structure:

```json
{
  "expense": "Bought groceries",
  "category": "Food & Groceries",
  "confidence": 0.XX
}
```

## Invalid Input Example

```json
{
  "expense": ""
}
```

Expected response:

```json
{
  "error": "Expense description is required"
}
```

## Testing Tools

- Postman
- Flask development server
- Python / Scikit-learn

> Mark a test as Pass only after actually running it. Replace expected results with actual results when testing is completed.
