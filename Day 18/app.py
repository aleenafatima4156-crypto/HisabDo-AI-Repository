from flask import Flask, request, jsonify
from services.financial_alerts import generate_smart_financial_alerts
import pandas as pd
from services.daily_business_brief import generate_daily_business_brief
from services.payment_reminders import generate_payment_reminders
from services.customer_followup import generate_customer_followup_suggestions

from services.context_suggestions import (
    generate_context_aware_suggestion
)
from services.feature_discovery import discover_features
from services.financial_goals import track_financial_goal
from services.personalized_action_plan import generate_action_plan
from services.business_health import calculate_business_health
from services.predictive_expense_alerts import (
    generate_predictive_expense_alert
)
from services.customer_risk_signals import (
    generate_customer_risk_signal
)

from services.notification_prioritization import (
    prioritize_notifications
)
from services.monthly_insights import (
    generate_monthly_insights
)
from services.personalized_ai_dashboard import (
    generate_ai_dashboard
)
from services.recommendations import generate_personalized_recommendation


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "HisabDo AI API is running"
    })


@app.route("/ai/personalized-recommendation", methods=["POST"])
def personalized_recommendation():

    try:

        data = request.get_json()

        if not data or "expenses" not in data:
            return jsonify({
                "status": "error",
                "message": "Expenses data is required."
            }), 400

        df = pd.DataFrame(data["expenses"])

        required_columns = [
            "amount",
            "category"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:

            return jsonify({
                "status": "error",
                "message": "Missing required fields.",
                "missing_fields": missing_columns
            }), 400

        result = generate_personalized_recommendation(df)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    
@app.route("/ai/smart-financial-alerts", methods=["POST"])
def smart_financial_alerts():

    try:

        data = request.get_json()

        if not data or "expenses" not in data:

            return jsonify({
                "status": "error",
                "message": "Expenses data is required."
            }), 400

        df = pd.DataFrame(data["expenses"])

        required_columns = [
            "amount",
            "category"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:

            return jsonify({
                "status": "error",
                "message": "Missing required fields.",
                "missing_fields": missing_columns
            }), 400

        result = generate_smart_financial_alerts(df)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500    


@app.route("/ai/daily-business-brief", methods=["POST"])
def daily_business_brief():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "Business data is required."
            }), 400

        required_fields = [
            "sales",
            "expenses",
            "customers",
            "pending_payments"
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in data
        ]

        if missing_fields:

            return jsonify({
                "status": "error",
                "message": "Missing required fields.",
                "missing_fields": missing_fields
            }), 400

        result = generate_daily_business_brief(data)

        return jsonify(result)

    except ValueError:

        return jsonify({
            "status": "error",
            "message": "Sales, expenses, customers and pending payments must contain valid numbers."
        }), 400

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    
@app.route("/ai/payment-reminders", methods=["POST"])
def payment_reminders():

    try:

        data = request.get_json()

        if not data or "payments" not in data:

            return jsonify({
                "status": "error",
                "message": "Payment data is required."
            }), 400

        df = pd.DataFrame(data["payments"])

        result = generate_payment_reminders(df)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/customer-followup", methods=["POST"])
def customer_followup():

    try:

        data = request.get_json()

        if not data or "customers" not in data:

            return jsonify({
                "status": "error",
                "message": "Customer data is required."
            }), 400

        df = pd.DataFrame(data["customers"])

        result = generate_customer_followup_suggestions(df)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/context-suggestion", methods=["POST"])
def context_suggestion():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "Request data is required."
            }), 400

        if "current_expense" not in data:
            return jsonify({
                "status": "error",
                "message": "Current expense is required."
            }), 400

        recent_expenses = data.get(
            "recent_expenses",
            []
        )

        result = generate_context_aware_suggestion(
            data["current_expense"],
            recent_expenses
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/feature-discovery", methods=["POST"])
def feature_discovery():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "User activity data is required."
            }), 400

        result = discover_features(data)

        return jsonify(result)

    except ValueError:

        return jsonify({
            "status": "error",
            "message": "Activity values must contain valid numbers."
        }), 400

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/financial-goal", methods=["POST"])
def financial_goal():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Financial goal data is required."
            }), 400

        result = track_financial_goal(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/action-plan", methods=["POST"])
def action_plan():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Action plan data is required."
            }), 400

        result = generate_action_plan(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/business-health", methods=["POST"])
def business_health():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Business data is required."
            }), 400

        result = calculate_business_health(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    

@app.route("/ai/predictive-expense-alert", methods=["POST"])
def predictive_expense_alert():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Expense data is required."
            }), 400

        result = generate_predictive_expense_alert(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/customer-risk", methods=["POST"])
def customer_risk():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Customer data is required."
            }), 400

        result = generate_customer_risk_signal(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/notification-priority", methods=["POST"])
def notification_priority():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Notification data is required."
            }), 400

        notifications = data.get(
            "notifications"
        )

        if notifications is None:

            return jsonify({
                "status": "error",
                "message": "Notifications list is required."
            }), 400

        result = prioritize_notifications(
            notifications
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/monthly-insights", methods=["POST"])
def monthly_insights():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Monthly data is required."
            }), 400

        result = generate_monthly_insights(
            data
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/ai/dashboard", methods=["POST"])
def ai_dashboard():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "Dashboard data is required."
            }), 400

        result = generate_ai_dashboard(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)