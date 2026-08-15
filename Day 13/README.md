# HisabDo – Day 13 AI/ML Capstone

## Smart Expense Categorization

### Intern
Aleena Fatima

### Track
AI / ML

---

## 1. Project Overview

This project develops an application-ready AI/ML service for HisabDo.

The selected feature is Smart Expense Categorization. It automatically
predicts an expense category from a user's expense description.

The service is exposed through a Flask REST API so that it can later
be integrated with the HisabDo Website, Web Application, and Mobile
Application.

---

## 2. Objective

The Day 13 objective is to prepare the Smart Expense Categorization
feature for integration with the Capstone application.

The implementation focuses on:

- Structured input handling
- AI request processing
- Response validation
- Error handling
- REST API/service layer
- Sample inputs and outputs
- UI interaction flow
- Website integration
- Web Application integration
- Mobile Application integration

---

## 3. AI Feature

### Smart Expense Categorization

The user provides an expense description such as:

"I bought groceries for dinner"

The AI service processes the text and predicts an appropriate expense
category.

Example:

Input:

I bought groceries for dinner

Output:

Food & Groceries

The API also returns a confidence score.

---

## 4. Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Flask | REST API/service layer |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Expense classification |
| Joblib | Model/vectorizer storage |
| Pandas | Dataset handling |
| Thunder Client | API testing |

---

## 5. System Architecture

User
↓
Website / Web Application / Mobile Application
↓
HisabDo Backend
↓
Flask REST API
↓
Input Validation
↓
TF-IDF
↓
Logistic Regression
↓
Category + Confidence
↓
Response Validation
↓
JSON Response
↓
Application

---

## 6. API Endpoint

### Endpoint

POST /categorize

### Local URL

http://127.0.0.1:5000/categorize

### Content Type

application/json

---

## 7. Input Format

Example:

{
    "user_id": "U001",
    "expense": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-14"
}

### Input Fields

- user_id – application user identifier
- expense – expense description used by the ML model
- amount – transaction amount
- currency – transaction currency
- date – transaction date

---

## 8. Output Format

Example:

{
    "status": "success",
    "user_id": "U001",
    "description": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-14",
    "category": "Food & Groceries",
    "confidence": 0.XX,
    "processing_time_seconds": 0.XX
}

The confidence and processing time values should be taken from the
actual API response during testing.

---

## 9. Error Handling

The API validates requests before sending the expense description
to the ML model.

### Handled Errors

- Missing JSON data
- Invalid request structure
- Missing expense description
- Empty expense description
- Non-string expense description
- Excessively long expense description
- Unavailable ML model
- Prediction failure
- Invalid AI response
- Unknown API endpoint

### Example

Input:

{
    "user_id": "U002",
    "amount": 4500,
    "currency": "PKR"
}

Response:

{
    "status": "error",
    "message": "Expense description is required"
}

---

## 10. Low Confidence Handling

The ML model calculates prediction probability.

If the confidence is below the configured threshold, the system
returns:

Uncategorized

This reduces the risk of presenting uncertain predictions as
reliable classifications.

---

## 11. Response Validation

The service verifies that important fields are present before returning
the response to the application.

Required fields include:

- status
- description
- category
- confidence

If the response does not contain the required fields, an error is
returned.

---

## 12. UI Flow

The planned user flow is:

User
↓
Add New Expense
↓
Enter Expense Description
↓
Analyze
↓
AI Categorization
↓
Display Category + Confidence
↓
Save Expense

Example:

User enters:

"I bought groceries for dinner"

↓

AI predicts:

Food & Groceries

↓

User reviews the result

↓

User saves the transaction.

---

## 13. Website Integration

The Website can communicate with the AI service through the backend.

Website
↓
Backend
↓
POST /categorize
↓
AI Service
↓
ML Model
↓
JSON Response
↓
Website

---

## 14. Web Application Integration

The Web Application can use the same REST API.

Web Application
↓
Backend/API
↓
AI Service
↓
ML Model
↓
Category + Confidence
↓
Web Application

---

## 15. Mobile Application Integration

The Mobile Application can send structured JSON data through the
HisabDo backend.

Mobile Application
↓
HisabDo Backend
↓
AI API
↓
ML Model
↓
Category + Confidence
↓
Mobile Application

---

## 16. API Cost

The current POC uses a locally hosted Machine Learning model.

Therefore:

- No external AI API is required.
- No per-request external AI API charge is required.
- The main infrastructure cost in production would be server/cloud
  hosting and maintenance.

If an external AI API is introduced later, API usage charges and
provider limits would need to be considered.

---

## 17. Response Latency

The API records processing time using:

processing_time_seconds

This value can be monitored during testing.

For a production system, latency should be monitored regularly to
ensure a responsive user experience.

---

## 18. Rate Limits

A production API should implement rate limiting.

Possible controls include:

- Requests per user
- Requests per IP
- Requests per minute
- Authentication-based limits

Rate limiting can help prevent API abuse and excessive resource usage.

---

## 19. Security Considerations

Because HisabDo handles financial information, security is important.

Recommended production controls include:

- HTTPS
- Authentication
- Authorization
- Input validation
- Secure database access
- Restricted access to financial records
- Secure logging
- Protection of API credentials
- Avoiding unnecessary sensitive information in logs

---

## 20. Data Privacy

Financial transaction information can be sensitive.

The system should:

- Collect only required information.
- Avoid unnecessary storage of personal information.
- Protect stored financial data.
- Restrict access to authorized users.
- Avoid sending financial data to external AI services unless necessary.
- Follow applicable privacy and data-protection requirements.

---

## 21. AI Error Handling

This is a classification model rather than a generative chatbot, so
traditional text hallucination is less relevant.

However, ML classification errors are possible.

To handle these:

- Return confidence scores.
- Use a low-confidence threshold.
- Return "Uncategorized" for uncertain predictions.
- Allow users to correct categories.
- Use corrected data for future model improvement.

---

## 22. Testing

The API was tested using Thunder Client.

Testing includes:

1. Successful expense categorization
2. Successful bill categorization
3. Missing expense validation
4. Empty expense validation
5. Invalid data type validation
6. API response validation

Screenshots of testing are included in the project submission.

---

## 23. Project Files

- app.py – Flask API
- expense_model.pkl – trained ML model
- tfidf_vectorizer.pkl – TF-IDF vectorizer
- api_documentation.md – API documentation
- sample_inputs_outputs.md – API testing examples
- integration_architecture.md – system integration architecture
- ui_flow.md – planned UI flow
- requirements.txt – Python dependencies
- screenshots/ – testing evidence

---

## 24. Future Improvements

- Larger and more diverse dataset
- Improved category coverage
- Multilingual expense descriptions
- User-specific learning
- Database integration
- Authentication and authorization
- Production HTTPS deployment
- Rate limiting
- Model monitoring
- Automated model retraining
- Direct Website integration
- Direct Web Application integration
- Mobile Application integration

---

## 25. Day 13 Completion Checklist

- [x] Updated AI POC
- [x] API/service endpoint
- [x] Structured input format
- [x] Structured output format
- [x] Response validation
- [x] Error handling
- [x] Sample inputs/outputs
- [x] UI interaction flow
- [x] Website integration plan
- [x] Web Application integration plan
- [x] Mobile Application integration plan
- [x] Architecture documentation
- [x] Security considerations
- [x] Data privacy considerations
- [x] API cost considerations
- [x] Response latency consideration
- [x] Rate-limit strategy
- [x] AI error handling
- [x] GitHub-ready project structure

---

## 26. Conclusion

The Day 13 implementation prepares the Smart Expense Categorization
feature for integration with the HisabDo application ecosystem.

The Flask-based AI service provides a structured REST interface,
validates incoming requests, processes expense descriptions using
TF-IDF and Logistic Regression, validates responses, handles errors,
and returns category and confidence information.

The same service can later be consumed by the HisabDo Website,
Web Application, and Mobile Application through the backend/API layer.