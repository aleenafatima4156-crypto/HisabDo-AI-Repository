from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_limiter.errors import RateLimitExceeded

from config import Config
from services.support.context_support import generate_context_help
from services.support.feature_guidance import get_feature_guidance
from services.support.step_help import generate_step_help
from services.support.error_assistance import generate_error_assistance
from services.support.help_articles import suggest_help_articles
from services.support.support_automation import automate_support
from services.support.escalation import escalate_to_human
from services.support.faq_service import search_faq
from services.support.related_questions import get_related_questions
from services.support.response_quality import improve_response

app = Flask(__name__)
CORS(app)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["100 per minute"]
)

def success_response(data=None, message="Success"):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), 200

def error_response(message, status_code=400):
    return jsonify({
        "status": "error",
        "message": message,
        "data": None
    }), status_code

@app.route("/", methods=["GET"])
def home():
    return success_response(
        {
            "service": Config.APP_NAME,
            "status": "running"
        },
        "HisabDo AI Help & Support API is running."
    )

@app.route("/ui", methods=["GET"])
def ui():
    from flask import render_template
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return success_response(
        {
            "service": Config.APP_NAME,
            "status": "healthy"
        },
        "API health check successful."
    )

@app.route("/api/info", methods=["GET"])
def api_info():
    return success_response(
        {
            "name": Config.APP_NAME,
            "version": Config.API_VERSION,
            "type": "REST API",
            "integration": ["Web Application", "Mobile Application"]
        },
        "API information retrieved successfully."
    )

@app.route("/ai/help/context", methods=["POST"])
def context_help():
    try:
        data = request.get_json(silent=True)
        if not data:
            return error_response("Help request data is required.", 400)
        return success_response(
            generate_context_help(data),
            "Context-aware help generated."
        )
    except Exception:
        return error_response("Unable to process context help request.", 500)

@app.route("/ai/help/feature", methods=["POST"])
def feature_guidance():
    try:
        data = request.get_json(silent=True)
        if not data:
            return error_response("Feature guidance data is required.", 400)
        return success_response(
            get_feature_guidance(data),
            "Feature guidance generated."
        )
    except Exception:
        return error_response("Unable to process feature guidance request.", 500)

@app.route("/ai/help/steps", methods=["POST"])
def step_help():
    try:
        data = request.get_json(silent=True)
        if not data:
            return error_response("Step-help data is required.", 400)
        return success_response(
            generate_step_help(data),
            "Step-by-step help generated."
        )
    except Exception:
        return error_response("Unable to process step-help request.", 500)

@app.route("/ai/help/error", methods=["POST"])
def error_assistance():
    try:
        data = request.get_json(silent=True)
        if not data:
            return error_response("Error assistance data is required.", 400)
        return success_response(
            generate_error_assistance(data),
            "Error assistance generated."
        )
    except Exception:
        return error_response("Unable to process error assistance request.", 500)

@app.route("/ai/help/articles", methods=["POST"])
def help_articles():
    try:
        data = request.get_json(silent=True)
        if not data:
            return error_response("Article search data is required.", 400)
        return success_response(
            suggest_help_articles(data),
            "Help articles suggested."
        )
    except Exception:
        return error_response("Unable to process article request.", 500)

@app.route("/ai/help/automate", methods=["POST"])
def support_automation():
    try:
        data = request.get_json(silent=True)
        if not data:
            return error_response("Support automation data is required.", 400)
        return success_response(
            automate_support(data),
            "Support request automated."
        )
    except Exception:
        return error_response("Unable to process automation request.", 500)

@app.route("/ai/help/escalate", methods=["POST"])
def human_escalation():
    try:
        data = request.get_json(silent=True)
        if not data:
            return error_response("Escalation data is required.", 400)
        return success_response(
            escalate_to_human(data),
            "Support request escalated."
        )
    except Exception:
        return error_response("Unable to process escalation request.", 500)

@app.route("/ai/help/faq", methods=["POST"])
@limiter.limit("20 per minute")
def faq_help():
    try:
        data = request.get_json(silent=True)
        if not data:
            return error_response("Request data is required.", 400)

        query = str(data.get("query", "")).strip()
        if not query:
            return error_response("FAQ query is required.", 400)
        if len(query) > 500:
            return error_response(
                "Query must not exceed 500 characters.", 400
            )

        result = improve_response(search_faq(query))

        if result.get("found"):
            result["related_questions"] = get_related_questions(
                query, result.get("category")
            )
        else:
            result["related_questions"] = []

        return success_response(
            result,
            "AI support response generated."
        )
    except Exception:
        return error_response("Unable to process support request.", 500)

@app.errorhandler(404)
def not_found(error):
    return error_response("API endpoint not found.", 404)

@app.errorhandler(405)
def method_not_allowed(error):
    return error_response("HTTP method not allowed.", 405)

@app.errorhandler(RateLimitExceeded)
def rate_limit_exceeded(error):
    return error_response(
        "Too many requests. Please try again later.", 429
    )

if __name__ == "__main__":
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
