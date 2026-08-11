import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# 1. Load Dataset


data = pd.read_csv(
    r"C:\Users\human\Desktop\task 10\expense_category_dataset_500.csv"
)

print("Dataset loaded successfully!")
print("Total records:", len(data))

print("\nCategory distribution:")
print(data["category"].value_counts())


# 2. Separate Input and Target

X = data["expense"]
y = data["category"]


# ==========================================
# 3. Train/Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 4. Baseline Model
# ==========================================

# Majority class = dataset ki sabse common category

majority_class = y_train.value_counts().idxmax()

baseline_predictions = [majority_class] * len(y_test)

baseline_accuracy = accuracy_score(
    y_test,
    baseline_predictions
)

print("\n========== BASELINE ==========")
print("Majority Class:", majority_class)
print(f"Baseline Accuracy: {baseline_accuracy:.4f}")


# ==========================================
# 5. TF-IDF Feature Extraction
# ==========================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)

X_test_tfidf = vectorizer.transform(X_test)

print("\nTF-IDF feature extraction completed!")


# ==========================================
# 6. Train Logistic Regression Model
# ==========================================

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train_tfidf,
    y_train
)

print("Model training completed!")


# ==========================================
# 7. Predictions
# ==========================================

y_pred = model.predict(X_test_tfidf)


# ==========================================
# 8. Model Evaluation
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)


print("\n========== MODEL EVALUATION ==========")

print(f"Accuracy          : {accuracy:.4f}")
print(f"Precision         : {precision:.4f}")
print(f"Recall            : {recall:.4f}")
print(f"F1 Score          : {f1:.4f}")

print("\n========== MODEL VS BASELINE ==========")

print(f"Baseline Accuracy : {baseline_accuracy:.4f}")
print(f"Model Accuracy    : {accuracy:.4f}")

if accuracy > baseline_accuracy:
    print("Result: ML model performs better than the baseline.")
elif accuracy == baseline_accuracy:
    print("Result: ML model performs equal to the baseline.")
else:
    print("Result: Baseline performs better than the ML model.")


# ==========================================
# 9. Confusion Matrix
# ==========================================

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=model.classes_
)

print("\n========== CONFUSION MATRIX ==========")
print(cm)


# ==========================================
# 10. Save Confusion Matrix
# ==========================================

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

disp.plot(
    xticks_rotation=45
)

plt.title(
    "Smart Expense Categorization - Confusion Matrix"
)

plt.tight_layout()

plt.savefig(
    "model_evaluation.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nConfusion matrix saved as model_evaluation.png")

plt.show()


# ==========================================
# 11. Save Trained Model
# ==========================================

joblib.dump(
    model,
    "expense_model.pkl"
)

joblib.dump(
    vectorizer,
    "tfidf_vectorizer.pkl"
)

print("\nModel saved as expense_model.pkl")
print("TF-IDF vectorizer saved as tfidf_vectorizer.pkl")


# ==========================================
# 12. Test Sample Prediction
# ==========================================

sample_expense = [
    "I bought groceries for dinner"
]

sample_vector = vectorizer.transform(
    sample_expense
)

prediction = model.predict(
    sample_vector
)[0]

probabilities = model.predict_proba(
    sample_vector
)[0]

confidence = max(probabilities)


print("\n========== SAMPLE PREDICTION ==========")

print(
    "Input:",
    sample_expense[0]
)

print(
    "Predicted Category:",
    prediction
)

print(
    "Confidence:",
    round(float(confidence), 4)
)


# ==========================================
# 13. Final Summary
# ==========================================

print("\n========================================")
print("DAY 10 ML TRAINING COMPLETED")
print("========================================")

print("Dataset Records:", len(data))
print("Categories:", len(model.classes_))
print("Baseline Accuracy:", round(baseline_accuracy, 4))
print("Model Accuracy:", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("F1 Score:", round(f1, 4))

print("\nGenerated Files:")
print("1. expense_model.pkl")
print("2. tfidf_vectorizer.pkl")
print("3. model_evaluation.png")

print("\nReady for Flask API integration!")