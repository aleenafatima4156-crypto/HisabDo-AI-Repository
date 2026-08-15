# HisabDo – Day 14 AI/ML Capstone

## Smart Expense Categorization

### Intern
Aleena Fatima

### Track
AI / ML

---

# 1. Project Overview

The Day 14 project continues the development of the Smart Expense
Categorization feature for HisabDo.

The system accepts a user's expense description through a REST API,
validates the request, sends the description to a dedicated AI service,
processes it using TF-IDF and Logistic Regression, and returns the
predicted expense category with a confidence score.

The objective is to move the AI feature toward practical application
integration.

---

# 2. Day 14 Objectives

The implementation covers:

- Continued AI feature development
- Dedicated AI service layer
- Structured API requests
- Input validation
- AI request processing
- Response validation
- Error handling
- End-to-end workflow
- Website integration planning
- Web Application integration planning
- Mobile Application integration planning

---

# 3. Selected AI Feature

## Smart Expense Categorization

The feature automatically predicts an expense category from a user's
expense description.

Example:

Input:

I bought groceries for dinner

Output:

Food & Groceries

The system also returns a confidence score.

---

# 4. Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Flask | REST API |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Expense classification |
| Joblib | Model loading |
| Pandas | Dataset processing |
| Thunder Client | API testing |

---

# 5. Architecture

User
↓
Website / Web Application / Mobile Application
↓
Backend / API
↓
Flask API
↓
Input Validation
↓
AI Service
↓
TF-IDF
↓
Logistic Regression
↓
Prediction + Confidence
↓
Response Validation
↓
JSON Response
↓
Application

---

# 6. Project Structure

Day14/

├── app.py

├── ai_service.py

├── expense_model.pkl

├── tfidf_vectorizer.pkl

├── requirements.txt

├── README.md

├── end_to_end_demo.md

├── integration_document.md

└── screenshots/

    ├── success.png
    ├── missing_expense.png
    ├── empty_expense.png
    └── invalid_type.png

---

# 7. API Service Layer

The main API endpoint is:

POST /categorize

Local development URL:

http://127.0.0.1:5000/categorize

The Flask application handles:

- HTTP requests
- Input validation
- Error handling
- AI service communication
- Response validation

The actual ML processing is separated into:

ai_service.py

This provides a basic service-layer architecture.

---

# 8. Input Format

Example:

{
    "user_id": "U001",
    "expense": "I bought groceries for dinner",
    "amount": 2500,
    "currency": "PKR",
    "date": "2026-08-14"
}

Input fields:

- user_id
- expense
- amount
- currency
- date

The expense field is required for AI classification.

---

# 9. Input Validation

The API validates:

- JSON request
- Request structure
- Expense existence
- Expense data type
- Empty descriptions
- Maximum description length

Invalid requests receive an appropriate error response.

---

# 10. AI Processing

The AI service performs the following operations:

1. Receive expense description
2. Validate the text
3. Convert text using TF-IDF
4. Send features to Logistic Regression
5. Generate category prediction
6. Calculate confidence
7. Apply confidence threshold
8. Return category and confidence

---

# 11. Low Confidence Handling

The system uses a confidence threshold.

Current threshold:

0.40

If model confidence is below the threshold, the system returns:

Uncategorized

This helps prevent uncertain predictions from being presented as
high-confidence results.

---

# 12. Output Format

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

Note:

The confidence and processing-time values should be replaced with the
actual values obtained during API testing.

---

# 13. Response Validation

Before returning a successful response, the API checks that important
fields are available.

Required response fields include:

- status
- description
- category
- confidence

If required fields are missing, the API returns an error response.

---

# 14. Error Handling

The API handles:

### Missing JSON

Returns an error when the request is not JSON.

### Missing Expense

Returns:

{
    "status": "error",
    "message": "Expense description is required"
}

### Empty Expense

Returns:

{
    "status": "error",
    "message": "Expense description cannot be empty"
}

### Invalid Expense Type

Returns:

{
    "status": "error",
    "message": "Expense must be a string"
}

### Long Expense Description

Descriptions longer than the configured limit are rejected.

### AI Service Failure

Unexpected ML processing errors are handled by the API.

---

# 15. End-to-End Workflow

The complete workflow is:

User enters expense
↓
Application sends JSON request
↓
Flask API receives request
↓
Input validation
↓
AI service
↓
TF-IDF processing
↓
Logistic Regression
↓
Prediction
↓
Confidence calculation
↓
Low-confidence check
↓
Response validation
↓
JSON response
↓
Application displays result

Detailed workflow is documented in:

end_to_end_demo.md

---

# 16. Website Integration

Website
↓
HisabDo Backend
↓
POST /categorize
↓
AI Service
↓
ML Model
↓
Category + Confidence
↓
Backend
↓
Website

The website can use the API to automatically categorize expenses before
saving transactions.

---

# 17. Web Application Integration

Web Application
↓
Backend API
↓
AI Service
↓
ML Model
↓
Prediction + Confidence
↓
Web Application

The web application can display the suggested category to the user.

---

# 18. Mobile Application Integration

Mobile Application
↓
HisabDo Backend
↓
AI API
↓
ML Model
↓
JSON Response
↓
Mobile Application

The mobile application can send expense information through a secure
backend/API connection.

---

# 19. External AI API

The current POC does not require an external AI API.

The ML model is locally hosted and accessed through the Python service.

This reduces dependency on external AI providers for the current
prototype.

---

# 20. Database

The current POC focuses on AI categorization.

In a production HisabDo system, a database can store:

- User transactions
- Predicted categories
- User corrections
- Model results
- Transaction dates
- Amounts

User corrections could later be used for model improvement.

---

# 21. Security Considerations

Financial information should be protected.

Production implementation should include:

- HTTPS
- Authentication
- Authorization
- Secure database access
- API access control
- Secure logging
- Protection of credentials
- Input validation
- Rate limiting

---

# 22. Data Privacy

The system should minimize collection and storage of unnecessary
personal information.

Financial transaction data should only be accessible to authorized
users and services.

External AI services should not receive financial information unless
required and properly secured.

---

# 23. API Cost

The current POC uses a local ML model.

Therefore, there is no per-request external AI API cost.

Production costs would mainly include:

- Server/cloud hosting
- Database
- Monitoring
- Maintenance
- Scaling

---

# 24. Response Latency

The API calculates:

processing_time_seconds

This can be used to monitor prediction performance.

Production monitoring should track API latency and identify slow
requests.

---

# 25. Rate Limiting

A production deployment should limit excessive API requests.

Possible controls include:

- Requests per user
- Requests per IP
- Requests per minute
- Authentication-based limits

---

# 26. Testing

The API was tested using Thunder Client.

Testing includes:

- Successful categorization
- Missing expense
- Empty expense
- Invalid expense type

Testing screenshots are stored in the screenshots folder.

---

# 27. End-to-End Demonstration

Example:

User enters:

I bought groceries for dinner

Application sends:

POST /categorize

The API validates the request.

The AI service processes the description.

TF-IDF converts the text into numerical features.

Logistic Regression predicts the category.

The API calculates confidence.

The validated JSON response is returned to the application.

The application can then display:

Food & Groceries

---

# 28. Future Improvements

Future development can include:

- Larger dataset
- More expense categories
- Multilingual support
- User-specific learning
- Database integration
- Authentication
- HTTPS deployment
- API rate limiting
- Model monitoring
- Automated retraining
- User feedback-based model improvement
- Production Website integration
- Production Web Application integration
- Production Mobile Application integration

---

# 29. Day 14 Completion Checklist

- [x] AI feature continued
- [x] AI service layer created
- [x] Flask API created
- [x] Structured input handling
- [x] Input validation
- [x] AI request processing
- [x] Response validation
- [x] Error handling
- [x] Confidence handling
- [x] End-to-end workflow
- [x] Website integration documented
- [x] Web Application integration documented
- [x] Mobile Application integration documented
- [x] API testing
- [x] Error testing
- [x] Technical documentation
- [x] GitHub-ready structure

---

# 30. Conclusion

The Day 14 implementation moves the Smart Expense Categorization
feature from a basic ML POC toward an application-ready AI service.

The system now separates API handling from AI processing through a
dedicated service layer, validates requests and responses, handles
errors, calculates confidence, and documents integration with the
HisabDo Website, Web Application, and Mobile Application.

The architecture provides a foundation for future production
deployment and integration.