# Knowledge Base / Data Sources

## Training Dataset

The AI model is trained using a labeled expense category dataset containing expense descriptions and their corresponding categories.

| Expense Description | Category |
|---|---|
| Bought groceries | Food & Groceries |
| Paid electricity bill | Bills & Utilities |
| Filled petrol | Transportation |
| Bought new shoes | Shopping |
| Paid university fee | Education |

## Dataset Structure

```text
expense,category
```

Example:

```text
bought groceries,Food & Groceries
paid electricity bill,Bills & Utilities
filled petrol,Transportation
bought new shoes,Shopping
```

## Data Processing

Pandas is used for loading and processing the dataset. TF-IDF converts expense descriptions into numerical features, while the category is used as the target label.

## Knowledge Source

The model's primary knowledge comes from labeled expense examples in the training dataset. It does not require a traditional external knowledge base.

## Important Note

Prediction quality depends on dataset quality, diversity, and representation of different expense types.
