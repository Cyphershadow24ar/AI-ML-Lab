import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([0, 10, 20, 30, 40]).reshape(-1, 1)
y = np.array([14, 52, 95, 133, 171])

model = LinearRegression()
model.fit(X, y)

theta0 = model.intercept_
theta1 = model.coef_[0]


y_pred = model.predict(X)

residuals = y - y_pred
SSE = np.sum(residuals**2)

print("Estimated Intercept (θ0):", round(theta0, 3))
print("Estimated Slope (θ1):", round(theta1, 3))
print("Predicted Values:", np.round(y_pred, 2))
print("Residuals:", np.round(residuals, 2))
print("Sum of Squared Errors (SSE):", round(SSE, 3))

plt.scatter(X, y, color='blue', label='Given data points')
plt.plot(X, y_pred, color='red', label='Fitted regression line')
plt.title('Linear Regression: Y = 4X + 13 + s(0,1)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()