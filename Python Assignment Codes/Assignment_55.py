import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# ==========================================
# 1. LOAD THE DATASET
# ==========================================
# Try loading the CSV file; create a synthetic dataset if file is not present

try:
    df = pd.read_csv('Customer_Loan_Approval.csv')
    print("Dataset successfully loaded from 'Customer_Loan_Approval.csv'")
except FileNotFoundError:
    print("File not found. Generating sample Customer Loan Approval dataset...")
    np.random.seed(42)
    data_size = 500
    df = pd.DataFrame({
        'Age': np.random.randint(21, 65, size=data_size),
        'Income': np.random.randint(20000, 150000, size=data_size),
        'Credit Score': np.random.randint(300, 850, size=data_size),
        'Existing Loan': np.random.choice([0, 1], size=data_size),
        'Employment Experience': np.random.randint(0, 30, size=data_size),
        'Loan Amount': np.random.randint(5000, 50000, size=data_size),
        'LoanApproved': np.random.choice([0, 1], size=data_size, p=[0.4, 0.6])
    })

# ==========================================
# 2. CHECK FOR MISSING VALUES
# ==========================================

print("\nMissing values count per column:")
print(df.isnull().sum())

# Fill missing values if any
df.fillna(df.median(numeric_only=True), inplace=True)

# ==========================================
# 3. SEPARATE INPUT AND OUTPUT VARIABLES
# ==========================================

X = df.drop(columns=['LoanApproved'])
y = df['LoanApproved']

# Feature scaling for distance and gradient-based models (Logistic Regression & KNN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# 4. SPLIT DATASET INTO TRAIN & TEST SETS
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# ==========================================
# 5, 6, 7. INITIALIZE INDIVIDUAL MODELS
# ==========================================

log_reg = LogisticRegression(random_state=42)
dt_clf = DecisionTreeClassifier(random_state=42)
knn_clf = KNeighborsClassifier(n_neighbors=5)

# Train individual models
log_reg.fit(X_train, y_train)
dt_clf.fit(X_train, y_train)
knn_clf.fit(X_train, y_train)

# ==========================================
# 8. CALCULATE INDIVIDUAL ACCURACIES
# ==========================================

acc_log_reg = accuracy_score(y_test, log_reg.predict(X_test))
acc_dt = accuracy_score(y_test, dt_clf.predict(X_test))
acc_knn = accuracy_score(y_test, knn_clf.predict(X_test))

# ==========================================
# 9 & 10. HARD VOTING CLASSIFIER
# ==========================================

hard_voting = VotingClassifier(
    estimators=[
        ('lr', log_reg),
        ('dt', dt_clf),
        ('knn', knn_clf)
    ],
    voting='hard'
)
hard_voting.fit(X_train, y_train)
acc_hard_voting = accuracy_score(y_test, hard_voting.predict(X_test))

# ==========================================
# 11 & 12. SOFT VOTING CLASSIFIER
# ==========================================

soft_voting = VotingClassifier(
    estimators=[
        ('lr', log_reg),
        ('dt', dt_clf),
        ('knn', knn_clf)
    ],
    voting='soft'
)
soft_voting.fit(X_train, y_train)
acc_soft_voting = accuracy_score(y_test, soft_voting.predict(X_test))

# ==========================================
# 13. COMPARE RESULTS
# ==========================================
comparison_table = pd.DataFrame({
    'Model': [
        'Logistic Regression',
        'Decision Tree',
        'KNN',
        'Hard Voting',
        'Soft Voting'
    ],
    'Accuracy': [
        f"{acc_log_reg:.4f}",
        f"{acc_dt:.4f}",
        f"{acc_knn:.4f}",
        f"{acc_hard_voting:.4f}",
        f"{acc_soft_voting:.4f}"
    ]
})

print("\n" + "="*35)
print("     ACCURACY COMPARISON TABLE     ")
print("="*35)
print(comparison_table.to_string(index=False))