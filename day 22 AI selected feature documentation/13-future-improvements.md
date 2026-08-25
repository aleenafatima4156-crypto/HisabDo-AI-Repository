# Future Improvements

## 1. Larger and Better Dataset

Add more diverse real-world expense examples to improve generalization and handling of uncommon expenses.

## 2. Multilingual Support

Add English, Urdu, Roman Urdu, and mixed-language training examples.

Example:

`bijli ka bill pay kiya` → `Bills & Utilities`

## 3. Advanced NLP Models

Compare the current Logistic Regression approach with models such as:

- Random Forest
- Support Vector Machine
- Transformer-based NLP models
- Fine-tuned language models

## 4. Additional Features

Future versions can use:

- Amount
- Date
- Merchant
- Transaction history
- Previous user categories

## 5. User Feedback

Allow users to correct incorrect predictions. Corrected examples can be considered for future retraining.

## 6. Better Confidence Handling

For low-confidence predictions, ask the user to confirm or select a category.

## 7. Production Deployment

Deploy the API to a production environment and integrate it securely with the HisabDo website and mobile application.

## 8. Monitoring and Continuous Improvement

Monitor API response time, prediction accuracy, errors, low-confidence predictions, and user corrections to guide future model improvements.
