# HisabDo AI Help & Support System

A Flask REST API prototype for AI-powered user assistance.

## Features
- Context-aware assistance
- Feature guidance
- Step-by-step help
- Error assistance
- Help article suggestions
- FAQ support
- Confidence evaluation
- Related questions
- Support automation
- Human escalation
- Web UI
- Input validation
- Rate limiting
- Standardized JSON responses

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` if you want custom local settings.

## Run

```bash
python app.py
```

Open:

- UI: http://127.0.0.1:5000/ui
- Health: http://127.0.0.1:5000/health
- API info: http://127.0.0.1:5000/api/info

## Main POST endpoint

`POST /ai/help/faq`

```json
{
  "query": "How can I add an expense?"
}
```

## Testing

Use Thunder Client, Postman, or curl to test the endpoints.

## Note

This is a prototype using a local JSON knowledge base. Production deployment should add authentication, HTTPS, restricted CORS, persistent support tickets, monitoring, and a production-grade AI/semantic retrieval layer.
