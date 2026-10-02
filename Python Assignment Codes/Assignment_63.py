import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix, 
    classification_report, 
    precision_recall_fscore_support
)

# Set seed for reproducibility
np.random.seed(42)

# ==========================================
# Task 1: Load Dataset
# ==========================================
data = pd.read_csv("Loan_Default.csv")

print("--- Task 1: Dataset Head ---")
print(data.head())

# ==========================================
# Task 2: Exploratory Data Analysis
# ==========================================
print("\n--- Task 2: Dataset Info & Statistics ---")
print(data.info())
print("\nSummary Statistics:")
print(data.describe())

# ==========================================
# Task 3: Check Missing Values
# ==========================================
print("\n--- Task 3: Missing Values Count ---")
print(data.isnull().sum())

# ==========================================
# Task 4: Class Balance Check
# ==========================================
print("\n--- Task 4: Target Class Distribution ---")
print(data['Default'].value_counts(normalize=True))

# ==========================================
# Task 5: Categorical Encoding
# ==========================================
# Clean strings and map PreviousDefault to 1/0
if 'PreviousDefault' in data.columns:
    if data['PreviousDefault'].dtype == object:
        data['PreviousDefault'] = data['PreviousDefault'].astype(str).str.strip().str.capitalize()
        data['PreviousDefault'] = data['PreviousDefault'].map({'Yes': 1, 'No': 0})

# One-Hot Encoding for multi-category feature
data = pd.get_dummies(data, columns=['HomeOwnership'], drop_first=True)

# ==========================================
# Task 6: Separate Features (X) and Target (y)
# ==========================================
X = data.drop(columns=['Default'])
y = data['Default']

# Convert all features in X to numeric types explicitly
X = X.apply(pd.to_numeric, errors='coerce').fillna(0)

# ==========================================
# Task 7 & 8: Train-Test Split & Stratification
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ==========================================
# Task 9: Scale Features
# ==========================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# Task 10 & 11: Create & Train Baseline MLPClassifier
# ==========================================
mlp = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

mlp.fit(X_train_scaled, y_train)

# ==========================================
# Task 12 - 15: Model Evaluation
# ==========================================
y_pred = mlp.predict(X_test_scaled)

print("\n--- Task 12: Accuracy Score ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

print("\n--- Task 13: Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\n--- Task 14: Classification Report ---")
print(classification_report(y_test, y_pred))

precision, recall, f1, _ = precision_recall_fscore_support(
    y_test, y_pred, average='binary', zero_division=0
)
print(f"Task 15 Metrics -> Precision: {precision:.4f}, Recall: {recall:.4f}, F1-Score: {f1:.4f}")

# ==========================================
# Task 16: Plot Training Loss
# ==========================================
plt.figure(figsize=(8, 4))
plt.plot(mlp.loss_curve_, color='blue')
plt.title('Baseline MLP Training Loss Curve')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.grid(True)
plt.show()

# ==========================================
# Task 17: Test Model on New Loan Applicants
# ==========================================
raw_new_applicants = pd.DataFrame([
    {
        'Age': 28, 'Income': 35000, 'LoanAmount': 25000, 'CreditScore': 580,
        'EmploymentYears': 1, 'ExistingLoans': 3, 'MonthlyDebt': 1500, 'LoanTerm': 36,
        'PreviousDefault': 'Yes', 'HomeOwnership': 'Rent'
    },
    {
        'Age': 45, 'Income': 110000, 'LoanAmount': 15000, 'CreditScore': 780,
        'EmploymentYears': 12, 'ExistingLoans': 1, 'MonthlyDebt': 600, 'LoanTerm': 36,
        'PreviousDefault': 'No', 'HomeOwnership': 'Mortgage'
    }
])

raw_new_applicants['PreviousDefault'] = raw_new_applicants['PreviousDefault'].map({'Yes': 1, 'No': 0})
new_applicants_encoded = pd.get_dummies(raw_new_applicants, columns=['HomeOwnership'], drop_first=True)
new_applicants = new_applicants_encoded.reindex(columns=X.columns, fill_value=0)

new_applicants_scaled = scaler.transform(new_applicants)
predictions = mlp.predict(new_applicants_scaled)

print("\n--- Task 17: New Applicant Predictions ---")
for idx, pred in enumerate(predictions):
    risk_status = "1 -> High default risk" if pred == 1 else "0 -> Low default risk"
    print(f"Applicant {idx + 1}: {risk_status}")

# ==========================================
# Hyperparameter Experiments
# ==========================================
def evaluate_mlp(model):
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    prec, rec, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average='binary', zero_division=0
    )
    return acc, prec, rec, f1

# Experiment 1 — Activation Functions
print("\n=== Experiment 1: Activation Functions ===")
for act in ['identity', 'logistic', 'tanh', 'relu']:
    clf = MLPClassifier(hidden_layer_sizes=(32, 16), activation=act, solver='adam', max_iter=1000, random_state=42)
    acc, prec, rec, f1 = evaluate_mlp(clf)
    print(f"Activation: {act:<10} | Acc: {acc:.4f} | Precision: {prec:.4f} | Recall: {rec:.4f} | F1: {f1:.4f}")

# Experiment 2 — Hidden Layers
print("\n=== Experiment 2: Hidden Layer Configurations ===")
for arch in [(10,), (20, 10), (50, 25), (100, 50, 25)]:
    clf = MLPClassifier(hidden_layer_sizes=arch, activation='relu', solver='adam', max_iter=1000, random_state=42)
    acc, prec, rec, f1 = evaluate_mlp(clf)
    print(f"Layers: {str(arch):<15} | Acc: {acc:.4f} | Precision: {prec:.4f} | Recall: {rec:.4f} | F1: {f1:.4f}")

# Experiment 3 — Learning Rate Initializations
print("\n=== Experiment 3: Learning Rate Initializations ===")
for lr in [0.0001, 0.001, 0.01, 0.1]:
    clf = MLPClassifier(hidden_layer_sizes=(32, 16), activation='relu', solver='adam', learning_rate_init=lr, max_iter=1000, random_state=42)
    acc, prec, rec, f1 = evaluate_mlp(clf)
    print(f"LR Init: {lr:<8} | Acc: {acc:.4f} | Precision: {prec:.4f} | Recall: {rec:.4f} | F1: {f1:.4f}")