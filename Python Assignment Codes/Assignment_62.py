# Employee Attrition Prediction using MLPClassifier
# Deep Learning Based Employee Attrition Prediction System

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


# ---------------------------------------------------------
# 1. Load Dataset
# ---------------------------------------------------------

df = pd.read_csv("Employee_Attrition.csv")

print("Dataset loaded successfully.")
print()


# ---------------------------------------------------------
# 2. Display shape, columns and first five records
# ---------------------------------------------------------

print("Shape of Dataset:")
print(df.shape)
print()

print("Columns:")
print(df.columns)
print()

print("First Five Records:")
print(df.head())
print()


# ---------------------------------------------------------
# 3. Check Missing Values
# ---------------------------------------------------------

print("Missing Values:")
print(df.isnull().sum())
print()


# ---------------------------------------------------------
# 4. Identify Numerical and Categorical Features
# ---------------------------------------------------------

print("Numerical Features:")
print(df.select_dtypes(include=["int64", "float64"]).columns)
print()

print("Categorical Features:")
print(df.select_dtypes(include=["object"]).columns)
print()


# ---------------------------------------------------------
# 5. Convert categorical feature OverTime
# ---------------------------------------------------------

df["OverTime"] = df["OverTime"].map({
    "Yes": 1,
    "No": 0
})


# ---------------------------------------------------------
# 6. Convert target Attrition into 0 and 1
# ---------------------------------------------------------

df["Attrition"] = df["Attrition"].map({
    "Yes": 1,
    "No": 0
})


print("Dataset after conversion:")
print(df.head())
print()


# ---------------------------------------------------------
# 7. Separate Independent and Dependent Variables
# ---------------------------------------------------------

X = df.drop("Attrition", axis=1)

Y = df["Attrition"]


# ---------------------------------------------------------
# 8. Divide Dataset into Training and Testing Data
# ---------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)
print()


# ---------------------------------------------------------
# 9. Feature Scaling
# ---------------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# ---------------------------------------------------------
# 10. Create MLP with at least two hidden layers
# ---------------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=500,
    random_state=42
)


# ---------------------------------------------------------
# 11. Train the Network
# ---------------------------------------------------------

model.fit(X_train, Y_train)

print("Model training completed.")
print()


# ---------------------------------------------------------
# 12. Display Number of Iterations
# ---------------------------------------------------------

print("Number of iterations required for training:")
print(model.n_iter_)
print()


# ---------------------------------------------------------
# 13. Calculate Training Accuracy
# ---------------------------------------------------------

Y_train_pred = model.predict(X_train)

train_accuracy = accuracy_score(
    Y_train,
    Y_train_pred
)

print("Training Accuracy:")
print(train_accuracy * 100, "%")
print()


# ---------------------------------------------------------
# 14. Calculate Testing Accuracy
# ---------------------------------------------------------

Y_test_pred = model.predict(X_test)

test_accuracy = accuracy_score(
    Y_test,
    Y_test_pred
)

print("Testing Accuracy:")
print(test_accuracy * 100, "%")
print()


# ---------------------------------------------------------
# 15. Generate Confusion Matrix
# ---------------------------------------------------------

cm = confusion_matrix(
    Y_test,
    Y_test_pred
)

print("Confusion Matrix:")
print(cm)
print()

ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Stay", "Leave"]
).plot()

plt.title("Employee Attrition Confusion Matrix")
plt.show()


# ---------------------------------------------------------
# 16. Plot Loss Curve
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    model.loss_curve_
)

plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.title("MLP Training Loss Curve")

plt.grid()

plt.show()


# ---------------------------------------------------------
# 17. Prediction Function
# ---------------------------------------------------------

def Prediction(employee):

    employee_df = pd.DataFrame(
        [employee],
        columns=X.columns
    )

    employee_scaled = scaler.transform(employee_df)

    prediction = model.predict(employee_scaled)

    probability = model.predict_proba(employee_scaled)

    if prediction[0] == 1:

        print("Prediction: Employee is likely to leave.")

    else:

        print("Prediction: Employee is likely to stay.")

    print(
        "Probability of Leaving:",
        probability[0][1] * 100,
        "%"
    )


# ---------------------------------------------------------
# 18. Test using new employee record
# ---------------------------------------------------------

new_employee = {
    "Age": 25,
    "MonthlyIncome": 30000,
    "YearsAtCompany": 2,
    "TotalWorkingYears": 3,
    "DistanceFromHome": 10,
    "JobSatisfaction": 3,
    "WorkLifeBalance": 3,
    "OverTime": 1,
    "NumCompaniesWorked": 1,
    "TrainingTimesLastYear": 2
}

print("New Employee Prediction:")
Prediction(new_employee)


# ---------------------------------------------------------
# 19. Check Overfitting / Underfitting
# ---------------------------------------------------------

print()
print("Model Performance Analysis")
print("--------------------------")

print("Training Accuracy:", train_accuracy * 100, "%")
print("Testing Accuracy:", test_accuracy * 100, "%")

difference = train_accuracy - test_accuracy

if difference > 0.10:

    print("The model may be suffering from overfitting.")

elif train_accuracy < 0.70 and test_accuracy < 0.70:

    print("The model may be suffering from underfitting.")

else:

    print("The model does not show strong evidence of overfitting or underfitting.")