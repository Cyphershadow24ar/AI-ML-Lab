import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

np.random.seed(0)
n = 400
X1 = np.random.uniform(0, 2*np.pi, n)
X2 = np.random.uniform(0, 2*np.pi, n)
noise = np.random.normal(0, 1, n)   

Y = 10 * np.sin(X1) + 15 * np.sin(X2) + noise


A = np.column_stack([np.sin(X1), np.sin(X2)])   
df = pd.DataFrame(A, columns=['sinX1', 'sinX2'])
df['Y'] = Y


lr = LinearRegression(fit_intercept=True)
lr.fit(A, Y)
intercept = lr.intercept_
coefs = lr.coef_

y_pred = lr.predict(A)
residuals = Y - y_pred

SSE = np.sum(residuals**2)
MSE = mean_squared_error(Y, y_pred)
RMSE = np.sqrt(MSE)
R2 = r2_score(Y, y_pred)

print("SKLEARN OLS")
print("Intercept:", intercept)
print("Coefficients (sinX1, sinX2):", coefs)
print(f"Sum of residuals: {residuals.sum():.3e}")
print(f"SSE: {SSE:.6f}, MSE: {MSE:.6f}, RMSE: {RMSE:.6f}, R^2: {R2:.6f}")
print()


X_design = np.hstack([np.ones((n,1)), A])   
beta_hat = np.linalg.pinv(X_design.T @ X_design) @ X_design.T @ Y
print("NORMAL-EQN OLS (Intercept, coef_sinX1, coef_sinX2):")
print(beta_hat)


y_hat_ne = X_design @ beta_hat
res_ne = Y - y_hat_ne
print(f"Sum residuals (normal-eq): {res_ne.sum():.3e}, SSE: {np.sum(res_ne**2):.6f}")
print()


X_sm = sm.add_constant(A)     
sm_model = sm.OLS(Y, X_sm).fit()
print("STATSMODELS OLS SUMMARY (first lines):")
print(sm_model.summary().tables[0])
print()
print(sm_model.summary().tables[1])


print("\nNote: true coefficients on sin(X1), sin(X2) are 10 and 15 respectively.")
