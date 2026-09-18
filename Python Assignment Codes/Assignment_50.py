import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix, 
    classification_report
)

# ==========================================
# 1. LOAD AND EXPLORE THE DATASET
# ==========================================

data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

print("Dataset Shape:", X.shape)
print("\nFirst 5 rows of features:")
print(X.head())

# Target class counts: 0 -> Malignant, 1 -> Benign
print("\nTarget Class Distribution:")
print(y.value_counts().rename({0: 'Malignant (0)', 1: 'Benign (1)'}))

# ==========================================
# 2. DATA PREPROCESSING
# ==========================================
# Check for missing values

print("\nMissing values in dataset:", X.isnull().sum().sum())
# Impute missing values if any exist
X.fillna(X.mean(), inplace=True)

# Feature Scaling (Standardization)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# ==========================================
# 3. EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================
# Summary statistics

print("\nSummary Statistics:")
print(X.describe())

# Feature Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(X.corr(), cmap='coolwarm', annot=False)
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.show()

# ==========================================
# 4. TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

# ==========================================
# 5. BUILD MACHINE LEARNING MODEL
# ==========================================

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# ==========================================
# 6. MODEL EVALUATION
# ==========================================

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=['Malignant', 'Benign'])

print("\n" + "="*40)
print("EVALUATION METRICS")
print("="*40)
print(f"Accuracy Score: {acc * 100:.2f}%")

print("\nConfusion Matrix:")
print(cm)

# Plot Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Malignant (0)', 'Benign (1)'],
            yticklabels=['Malignant (0)', 'Benign (1)'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.show()

print("\nClassification Report (Precision, Recall, F1-Score):")
print(report)