# HisabDo AI Help & Support — Technical Documentation

## Implemented Capabilities
1. Context-aware assistance
2. Feature guidance
3. Step-by-step help
4. Error assistance
5. Help articles
6. FAQ support
7. Related question suggestions
8. Response confidence
9. Support automation
10. Human escalation
11. Web interface
12. REST API
13. Input validation
14. Rate limiting
15. Security/reliability documentation

## API Endpoints

| Method | Endpoint |
|---|---|
| GET | / |
| GET | /ui |
| GET | /health |
| GET | /api/info |
| POST | /ai/help/context |
| POST | /ai/help/feature |
| POST | /ai/help/steps |
| POST | /ai/help/error |
| POST | /ai/help/articles |
| POST | /ai/help/automate |
| POST | /ai/help/escalate |
| POST | /ai/help/faq |

## Validation
- Empty/missing request data returns HTTP 400.
- Empty FAQ query returns HTTP 400.
- FAQ query over 500 characters returns HTTP 400.
- Unknown endpoint returns HTTP 404.
- Unsupported method returns HTTP 405.

## Security
- Secrets are excluded through `.gitignore`.
- Production errors do not expose internal exception details.
- CORS is enabled for development; restrict origins in production.
- Sensitive financial data should be minimized.
- Production should use HTTPS, authentication, authorization and monitoring.

## Rate Limiting
Default: 100 requests/minute per client IP.
FAQ endpoint: 20 requests/minute per client IP.

## Future Improvements
- LLM integration
- Semantic embeddings/vector search
- Authentication
- Conversation history
- Multilingual support
- Production ticketing
- Analytics and monitoring
