# Known Limitations

## 1. Dataset Limitations

Model performance depends on the quality, size, and diversity of the training dataset.

## 2. Unfamiliar Expenses

Descriptions that are very different from training examples may be incorrectly classified.

## 3. Ambiguous Descriptions

Short or unclear inputs such as `Payment done` may not provide enough context for accurate categorization.

## 4. Language Limitation

If training data is mainly English, Urdu, Roman Urdu, and mixed-language inputs may have lower performance.

Example:

`bijli ka bill pay kiya`

## 5. Confidence Score Limitation

A high probability/confidence score does not guarantee that the prediction is correct.

## 6. Static Model

The trained model does not automatically learn from new user data unless a retraining pipeline is implemented.

## 7. Limited Context

The current model mainly uses expense description. Amount, date, merchant, and transaction history may not be included unless the model is redesigned to use them.

## 8. Production Limitations

A prototype may require additional production features such as authentication, HTTPS, rate limiting, monitoring, database integration, and model versioning.
