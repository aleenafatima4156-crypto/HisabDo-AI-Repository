import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ==============================
# 1. Sample Student Dataset
# ==============================

data = {
    "Attendance": [
        90, 85, 70, 60, 95,
        80, 65, 75, 88, 55,
        92, 78, 68, 82, 50,
        96, 73, 87, 62, 91
    ],

    "Assignment": [
        85, 80, 65, 55, 90,
        75, 60, 70, 82, 50,
        88, 72, 58, 78, 45,
        92, 68, 84, 57, 86
    ],

    "Midterm": [
        80, 78, 60, 50, 88,
        72, 55, 68, 81, 45,
        85, 70, 52, 75, 40,
        90, 65, 82, 48, 84
    ],

    "Final": [
        85, 82, 65, 52, 90,
        76, 58, 70, 85, 48,
        88, 74, 55, 79, 42,
        93, 68, 86, 50, 87
    ],

    "Result": [
        "Pass", "Pass", "Pass", "Fail", "Pass",
        "Pass", "Fail", "Pass", "Pass", "Fail",
        "Pass", "Pass", "Fail", "Pass", "Fail",
        "Pass", "Pass", "Pass", "Fail", "Pass"
    ]
}


# ==============================
# 2. Create DataFrame
# ==============================

df = pd.DataFrame(data)

print("Dataset loaded successfully!")
print(df)


# ==============================
# 3. Features and Target
# ==============================

X = df[
    [
        "Attendance",
        "Assignment",
        "Midterm",
        "Final"
    ]
]

y = df["Result"]


# ==============================
# 4. Train/Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==============================
# 5. Train Model
# ==============================

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train, y_train)


# ==============================
# 6. Evaluate
# ==============================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nModel Accuracy:", round(accuracy, 4))


# ==============================
# 7. Save Model
# ==============================

joblib.dump(
    model,
    "student_model.pkl"
)

print("\nModel saved as student_model.pkl")