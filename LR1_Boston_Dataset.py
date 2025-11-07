import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

boston = fetch_openml(name="boston", version=1, as_frame=True)
df = boston.frame

X = df[["RM"]]  
y = df["MEDV"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

theta0 = model.intercept_
theta1 = model.coef_[0]

print("Estimated Intercept (θ₀):", theta0)
print("Estimated Slope (θ₁):", theta1)

y_pred = model.predict(X_test)

residuals = y_test - y_pred
sse = np.sum(residuals ** 2)
sum_residuals = np.sum(residuals)

print("\nSum of residuals =", sum_residuals)
print("Sum of Squared Errors (SSE) =", sse)
print("Mean Squared Error (MSE) =", mean_squared_error(y_test, y_pred))
print("R² score =", r2_score(y_test, y_pred))

import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted Regression Line')
plt.xlabel("Average number of rooms per dwelling (RM)")
plt.ylabel("Median value of homes (MEDV)")
plt.title("Simple Linear Regression: MEDV vs RM")
plt.legend()
plt.show()