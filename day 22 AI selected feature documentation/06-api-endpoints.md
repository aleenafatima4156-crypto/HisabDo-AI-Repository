# API Endpoints & Request/Response Examples

## Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/predict` | Predict expense category |

## Request

```json
{
  "expense": "I bought pizza for dinner"
}
```

## Successful Response

```json
{
  "expense": "I bought pizza for dinner",
  "category": "Food & Groceries",
  "confidence": 0.92
}
```

> `0.92` is an example only. The actual confidence value must come from the trained model.

## Invalid Request

```json
{
  "expense": ""
}
```

Example validation response:

```json
{
  "error": "Expense description is required"
}
```

## Postman Testing

```text
Method: POST
URL: http://127.0.0.1:5000/predict
Content-Type: application/json
```

Request body:

```json
{
  "expense": "Paid electricity bill"
}
```
