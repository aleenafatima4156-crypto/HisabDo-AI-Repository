# HisabDo – Smart Expense Categorization AI

## Day 10 – AI/ML Capstone POC

### Track
AI / Machine Learning

### Project
HisabDo

### Selected AI Feature
Smart Expense Categorization

---

# 1. Project Overview

HisabDo is a financial management platform designed to help users manage
and organize their expenses.

This Day 10 project implements a proof-of-concept AI/ML feature that
automatically categorizes an expense based on its natural-language description.

For example:

> "I bought groceries for dinner"

can be automatically classified as:

> Food & Groceries

The system also provides a confidence score with the prediction.

---

# 2. Problem Statement

Users often have to manually select a category every time they enter an expense.

Manual categorization can:

- Take additional time
- Create inconsistent categorization
- Increase user effort
- Become inconvenient when many transactions are entered

The goal is to reduce this effort by automatically suggesting an appropriate
expense category.

---

# 3. Proposed AI Solution

The proposed solution uses Natural Language Processing and Machine Learning.

The expense description is converted into numerical text features using TF-IDF
and classified using Logistic Regression.

The system returns:

- Expense description
- Predicted category
- Confidence score

---

# 4. Input

The primary input is a text-based expense description.

Example:

```json
{
    "expense": "I bought groceries for dinner"
}