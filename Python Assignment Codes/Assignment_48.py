# Question 1

Border = "-"*50

# Dataset
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

n = len(X)

# 1. Mean of X
mean_x = sum(X) / n

# 2. Mean of Y
mean_y = sum(Y) / n

# 3. Slope (m) = sum((X - mean_x) * (Y - mean_y)) / sum((X - mean_x)^2)
numerator = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n))
denominator = sum((X[i] - mean_x) ** 2 for i in range(n))
m = numerator / denominator

# 4. Intercept (c) = mean_y - m * mean_x
c = mean_y - m * mean_x

print(f"Mean of X = {mean_x}")
print(f"Mean of Y = {mean_y}")
print()
print(f"Slope (m) = {m}")
print(f"Intercept (c) = {c}")
print()
print(f"Regression Equation:\nY = {m}X + {c}")
print()
print(Border)

# Predict Y for X = 6
x_new = 6
y_pred_6 = m * x_new + c
print(f"Predicted Y for X = 6 : {y_pred_6}")
print(Border)

# Question 2

# Dataset from Question 1
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]
n = len(X)

mean_x = sum(X) / n
mean_y = sum(Y) / n

m = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n)) / sum((X[i] - mean_x) ** 2 for i in range(n))
c = mean_y - m * mean_x

# 1. Predict all Y values using regression equation (Y_pred = m*X + c)
Y_pred = [m * x + c for x in X]

# Intermediate calculations
squared_errors = [(Y[i] - Y_pred[i]) ** 2 for i in range(n)]
total_variance = [(Y[i] - mean_y) ** 2 for i in range(n)]

# 2. Mean Squared Error (MSE)
mse = sum(squared_errors) / n

# R^2 Score = 1 - (SS_res / SS_tot)
ss_res = sum(squared_errors)
ss_tot = sum(total_variance)
r2_score = 1 - (ss_res / ss_tot)

print("Intermediate Calculations:")
print(f"{'X':<5} {'Y':<5} {'Y_pred':<10} {'(Y - Y_pred)^2':<18} {'(Y - Y_mean)^2':<15}")
print(Border)
for i in range(n):
    print(f"{X[i]:<5} {Y[i]:<5} {Y_pred[i]:<10.2f} {squared_errors[i]:<18.4f} {total_variance[i]:<15.4f}")

print("\nModel Performance Metrics:")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R^2 Score: {r2_score:.4f}")
print(Border)

# Question 3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1], [2], [3], [4], [5]])  # Experience
y = np.array([20000, 25000, 30000, 35000, 40000])  # Salary

# 1. Train linear regression model
model = LinearRegression()
model.fit(X, y)

# 2. Predict salary for 6 years of experience
exp_new = np.array([[6]])
predicted_salary = model.predict(exp_new)[0]
print(f"Predicted Salary for 6 Years Experience: ₹{int(predicted_salary)}")

# 3. Plot regression line using matplotlib
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary (₹)')
plt.title('Experience vs Salary Regression')
plt.legend()
plt.grid(True)
plt.show()