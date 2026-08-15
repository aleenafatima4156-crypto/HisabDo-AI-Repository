# Smart Expense Categorization – UI Flow

## User Flow

1. User opens the HisabDo application.
2. User selects Add Expense.
3. User enters an expense description.
4. User enters transaction details.
5. User selects Analyze.
6. The application sends the data to the AI API.
7. The AI service validates the request.
8. The ML model predicts the expense category.
9. The API returns category and confidence.
10. The application displays the prediction.
11. User can save the transaction.

## Example

User Input:

"I bought groceries for dinner"

↓

AI Processing

↓

Predicted Category:

"Food & Groceries"

↓

Confidence:

Actual API confidence value

↓

Save Expense