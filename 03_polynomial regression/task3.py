import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


housing = fetch_california_housing(as_frame=True)
data = housing.frame

feature_names = ["MedInc", "HouseAge", "AveRooms", "AveBedrms"]
x = data[feature_names]
y = housing.target

xtrain, xtest, ytrain, ytest = train_test_split(
	x, y, test_size=0.2, random_state=42
)

lin = LinearRegression()
lin.fit(xtrain, ytrain)
pred_lin = lin.predict(xtest)
r2_lin = r2_score(ytest, pred_lin)

lasso = Lasso(alpha=0.1)
lasso.fit(xtrain, ytrain)
pred_lasso = lasso.predict(xtest)
r2_lasso = r2_score(ytest, pred_lasso)

lasso_zeros = int(np.isclose(lasso.coef_, 0.0).sum())

print("R² на тестовій вибірці")
print(f"LinearRegression: {r2_lin:.4f}")
print(f"Lasso(alpha=0.1): {r2_lasso:.4f}")
print()

print("Коефіцієнти моделей")
print("Ознака      | LinearRegression | Lasso")
print("-" * 43)
for name, c_lin, c_lasso in zip(feature_names, lin.coef_, lasso.coef_, strict=True):
	print(f"{name:<10} | {c_lin:>15.6f} | {c_lasso:>10.6f}")

print()
print(f"Кількість коефіцієнтів, що стали 0 у Lasso: {lasso_zeros} із {len(feature_names)}")
