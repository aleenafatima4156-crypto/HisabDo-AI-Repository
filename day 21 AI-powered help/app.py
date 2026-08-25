from flask import Flask, request, jsonify
from services.support.feature_guidance import get_feature_guidance
from services.support.step_help import generate_step_help
from services.support.error_assistance import generate_error_assistance
from services.support.help_articles import suggest_help_articles
from services.support.support_automation import automate_support
from services.support.escalation import escalate_to_human

from services.support.context_support import generate_context_help


app = Flask(__name__)

# HOME / API STATUS


@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "success",
        "message": "HisabDo AI Help & Support API is running.",
        "feature": "Context-Aware User Assistance"
    })

# FEATURE 1
# CONTEXT-AWARE USER ASSISTANCE

@app.route("/ai/help/context", methods=["POST"])
def context_help():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Help request data is required."
            }), 400

        result = generate_context_help(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# 404 ERROR

@app.errorhandler(404)
def not_found(error):

    return jsonify({
        "status": "error",
        "message": "API endpoint not found."
    }), 404

# 405 ERROR

@app.errorhandler(405)
def method_not_allowed(error):

    return jsonify({
        "status": "error",
        "message": "HTTP method not allowed."
    }), 405

@app.route("/ai/help/feature", methods=["POST"])
def feature_guidance():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "Feature guidance data is required."
            }), 400

        result = get_feature_guidance(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/help/steps", methods=["POST"])
def step_help():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "Step-help data is required."
            }), 400

        result = generate_step_help(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    
@app.route("/ai/help/error", methods=["POST"])
def error_assistance():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Error assistance data is required."
            }), 400

        result = generate_error_assistance(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/help/articles", methods=["POST"])
def help_articles():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Article search data is required."
            }), 400

        result = suggest_help_articles(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500    

@app.route("/ai/help/automate", methods=["POST"])
def support_automation():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "Support automation data is required."
            }), 400

        result = automate_support(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/help/escalate", methods=["POST"])
def human_escalation():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Escalation data is required."
            }), 400

        result = escalate_to_human(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500    

# RUN FLASK APP


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )