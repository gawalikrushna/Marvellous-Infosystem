import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ==========================================
# 1. LOAD AND PREPARE THE DATASET
# ==========================================

try:
    df = pd.read_csv('Fraudulent_Transaction_Detection.csv')
    print("Dataset loaded successfully from 'Fraudulent_Transaction_Detection.csv'.")
except FileNotFoundError:
    print("File not found. Generating synthetic Fraudulent Transaction dataset...")
    np.random.seed(42)
    n_samples = 1000
    df = pd.DataFrame({
        'Transaction Amount': np.random.uniform(10, 5000, n_samples),
        'Transaction Time': np.random.uniform(0, 24, n_samples),
        'Account Age': np.random.randint(1, 120, n_samples),
        'Number of Previous Transactions': np.random.randint(0, 500, n_samples),
        'Location Difference': np.random.uniform(0, 1000, n_samples),
        'Device Type': np.random.choice(['Mobile', 'Desktop', 'Tablet'], n_samples),
        'Failed Login Attempts': np.random.randint(0, 5, n_samples),
        'Fraud': np.random.choice([0, 1], n_samples, p=[0.85, 0.15])
    })

# Encode categorical feature 'Device Type'

if 'Device Type' in df.columns and df['Device Type'].dtype == 'object':
    le = LabelEncoder()
    df['Device Type'] = le.fit_transform(df['Device Type'])

# Separate features and target

X = df.drop(columns=['Fraud'])
y = df['Fraud']

# Feature scaling

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# ==========================================
# 2. DEFINE AND TRAIN MODELS
# ==========================================

dt = DecisionTreeClassifier(random_state=42)
bagging = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=50, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
adaboost = AdaBoostClassifier(n_estimators=50, random_state=42)

# Voting Classifier incorporating base algorithms

voting = VotingClassifier(
    estimators=[
        ('dt', dt),
        ('rf', rf),
        ('adaboost', adaboost)
    ],
    voting='soft'
)

models = {
    'Decision Tree': dt,
    'Bagging': bagging,
    'Random Forest': rf,
    'AdaBoost': adaboost,
    'Voting': voting
}

# ==========================================
# 3. EVALUATE MODELS & PRINT CONFUSION MATRICES
# ==========================================

results = []

print("\n" + "="*45)
print("CONFUSION MATRICES & EVALUATION")
print("="*45)

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)
    
    results.append({
        'Algorithm': name,
        'Accuracy': f"{acc:.4f}",
        'Precision': f"{prec:.4f}",
        'Recall': f"{rec:.4f}",
        'F1': f"{f1:.4f}"
    })
    
    print(f"\n--- {name} ---")
    print("Confusion Matrix:")
    print(cm)

# ==========================================
# 4. FINAL COMPARISON TABLE
# ==========================================

comparison_df = pd.DataFrame(results)

print("\n" + "="*50)
print("             FINAL COMPARISON TABLE             ")
print("="*50)
print(comparison_df.to_string(index=False))