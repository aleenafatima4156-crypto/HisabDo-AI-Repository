# Setup & Installation

## Prerequisites

- Python 3.x
- VS Code
- pip
- Postman for API testing

## Example Project Structure

```text
HisabDo-AI/
├── app.py
├── expense_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── expense_category_dataset.csv
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate on Windows

```bash
venv\Scripts\activate
```

PowerShell alternative:

```bash
.\venv\Scripts\Activate.ps1
```

## Install Dependencies

```bash
pip install flask pandas scikit-learn joblib
```

Or:

```bash
pip install -r requirements.txt
```

## Run the Flask API

```bash
python app.py
```

Common local address:

```text
http://127.0.0.1:5000
```

## Test the API

```text
Method: POST
Endpoint: /predict
Content-Type: application/json
```

Example body:

```json
{
  "expense": "Bought groceries"
}
```

> Update filenames and commands to match the actual project structure.
