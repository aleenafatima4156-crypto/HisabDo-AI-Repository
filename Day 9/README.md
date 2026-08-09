# Day 9 – Smart Expense Categorization POC

## Primary AI Feature
Smart Expense Categorization automatically suggests a category for an expense description.

## Workflow
User → HisabDo Website/Web App/Mobile App → Categorization API → Text Validation → TF-IDF → Logistic Regression → Category + Confidence → Expense Record.

## Input
```json
{"description":"I bought pizza for dinner"}
```

## Output
```json
{"description":"I bought pizza for dinner","category":"Food & Groceries","confidence":0.XX}
```

## Technology
- Python: Project ki main programming language. Isse ML model aur API develop ki gayi hai.
- Scikit-learn: Machine Learning library jo TF-IDF aur Logistic Regression implement karne ke liye use hui.
- TF-IDF: Expense ke text ko numerical values mein convert karta hai taake ML model usay samajh sake.
- Logistic Regression: User ke expense ko different categories, jaise Food, Transport, Shopping etc. mein classify karta hai.
- Flask REST API: ML model ko API ke through accessible banata hai, taake website, web app ya mobile app is model ko use kar saken.

## Integration
The same API can be called by the Website, Web Application, or Mobile Application when a user creates an expense.

## Run
```bash
pip install -r requirements.txt
python app.py
```

API: `POST http://127.0.0.1:5000/categorize`

## Postman
Use Thunder Client `/categorize`, Body → raw → JSON:
```json
{"description":"I bought pizza for dinner"}
```

## Architecture
User → Application → API → TF-IDF → Logistic Regression → Prediction → Application/Database.

## Limitation
This is a proof-of-concept trained on a small sample dataset. A production model needs a larger, verified dataset and proper evaluation on unseen real transactions.

## Future Improvements
Add more categories, more real transaction data, multilingual/Urdu support, user feedback, confidence thresholds, and stronger NLP models.
