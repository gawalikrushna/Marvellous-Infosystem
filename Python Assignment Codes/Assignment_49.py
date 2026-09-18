Border = "-"*50

# Q1. Python program to calculate the Mean of a dataset using NumPy

import numpy as np

data = np.array([6, 7, 8, 9, 10, 11, 12])

mean = np.mean(data)

print(Border)
print("Dataset:", data)
print("Mean:", mean)
print(Border)

# Q2. Python program to calculate Variance and Standard Deviation

data = np.array([6, 7, 8, 9, 10, 11, 12])

variance = np.var(data)
standard_deviation = np.std(data)

print("Dataset:", data)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)

# Q3. Python program using StandardScaler

from sklearn.preprocessing import StandardScaler

data = np.array([
    [25, 200000],
    [30, 400000],
    [35, 800000]
])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print(Border)
print("Original Dataset:")
print(data)

print(Border)
print("\nScaled Dataset:")
print(scaled_data)

# Q4. Euclidean Distance Before and After Feature Scaling

from sklearn.preprocessing import StandardScaler

# Two points
A = np.array([25, 200000])
B = np.array([35, 800000])

# Distance before scaling
distance_before = np.linalg.norm(A - B)

print(Border)
print("Distance before scaling:", distance_before)

# Dataset for scaling
data = np.array([
    [25, 200000],
    [30, 400000],
    [35, 800000]
])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Distance after scaling
distance_after = np.linalg.norm(scaled_data[0] - scaled_data[2])

print(Border)
print("Distance after scaling:", distance_after)

# Q8. Python Program to Calculate TP, TN, FP, FN

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

TP = 0
TN = 0
FP = 0
FN = 0

for a, p in zip(actual, predicted):

    if a == 1 and p == 1:
        TP += 1

    elif a == 0 and p == 0:
        TN += 1

    elif a == 0 and p == 1:
        FP += 1

    elif a == 1 and p == 0:
        FN += 1

print(Border)
print("True Positive (TP):", TP)
print("True Negative (TN):", TN)
print("False Positive (FP):", FP)
print("False Negative (FN):", FN)

# Q9. Generate Classification Report Using Scikit-learn

from sklearn.metrics import classification_report

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

report = classification_report(actual, predicted)

print(Border)
print("Classification Report:")
print(report)

