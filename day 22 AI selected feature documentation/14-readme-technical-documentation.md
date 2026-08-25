# README & Technical Documentation Update

The GitHub `README.md` should provide enough information for a developer to understand, install, run, test, and integrate the AI Expense Categorization feature.

## Recommended README Sections

1. Project Title
2. Project Description
3. Features
4. Technology Stack
5. Installation
6. Running the Application
7. API Documentation
8. Project Architecture
9. Testing
10. Limitations
11. Future Improvements

## Project Title

`HisabDo – AI Expense Categorization`

## Features

- Automatic expense categorization
- TF-IDF text processing
- Logistic Regression classification
- Confidence score
- Input validation
- Flask REST API
- JSON response

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## API

```text
POST /predict
```

Example request:

```json
{
  "expense": "I bought pizza for dinner"
}
```

Example response:

```json
{
  "expense": "I bought pizza for dinner",
  "category": "Food & Groceries",
  "confidence": 0.XX
}
```

## Architecture

```text
User
 ↓
HisabDo App
 ↓
Flask API
 ↓
Validation
 ↓
TF-IDF
 ↓
Logistic Regression
 ↓
Category + Confidence
 ↓
JSON Response
```

## Documentation Checklist

- [ ] Project description added
- [ ] Installation instructions added
- [ ] API endpoint documented
- [ ] Request/response examples added
- [ ] Architecture added
- [ ] Technology stack listed
- [ ] Testing information added
- [ ] Limitations documented
- [ ] Future improvements documented

> Keep README details synchronized with the actual code, endpoint names, filenames, and implemented features.
