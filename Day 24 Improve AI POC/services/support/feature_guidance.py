GUIDANCE = {
    "expenses": "Open Expenses, choose Add Expense, enter the details, and save.",
    "invoices": "Open Invoices, choose Create Invoice, add customer and items, then save.",
    "reports": "Open Reports and select the report type you want to view.",
    "customers": "Open Customers and select Add Customer to create a new customer."
}

def get_feature_guidance(data):
    feature = str(data.get("feature", "")).strip()
    if not feature:
        return {"feature": None, "guidance": "Please provide a feature name."}

    key = feature.lower()
    return {
        "feature": feature,
        "guidance": GUIDANCE.get(
            key,
            f"Open the {feature} section and follow the available options."
        )
    }
