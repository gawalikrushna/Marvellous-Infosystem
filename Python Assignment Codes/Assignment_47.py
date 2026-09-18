# Question 7 & 8

Border = "-"*50

import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1], [2], [3], [4], [5]])  # Study Hours
y = np.array([50, 55, 60, 65, 70])  # Marks

# Train the regression model
model = LinearRegression()
model.fit(X, y)

# Print coefficient and intercept (Question 7)
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print(Border)

# Predict marks for 6 study hours (Question 8)
predicted_marks = model.predict([[6]])
print("Predicted Marks for 6 hours:", predicted_marks[0])
print(Border)

# Question 9

# Dataset (StudyHours, SleepHours)
X = np.array([[1, 7], [2, 6], [3, 7], [4, 6], [5, 8]])
y = np.array([50, 55, 60, 65, 70])

# Train the multiple linear regression model
model = LinearRegression()
model.fit(X, y)

# Print coefficients for both features and intercept
print("Coefficients (StudyHours, SleepHours):", model.coef_)
print("Intercept:", model.intercept_)

