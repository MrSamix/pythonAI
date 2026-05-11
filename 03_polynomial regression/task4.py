import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression, Ridge
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

models = [
	("LinearRegression", LinearRegression()),
	("Ridge(alpha=1.0)", Ridge(alpha=1.0)),
]

rows: list[tuple[str, float, int]] = []
for name, model in models:
	model.fit(xtrain, ytrain)
	pred = model.predict(xtest)
	r2_test = r2_score(ytest, pred)
	non_zero = int((~np.isclose(model.coef_, 0.0)).sum())
	rows.append((name, r2_test, non_zero))


print("Модель | Тест R² | Кількість ненульових коеф.")
print("-" * 48)
for name, r2_test, non_zero in rows:
	print(f"{name:<16} | {r2_test:>7.4f} | {non_zero:>24}")
