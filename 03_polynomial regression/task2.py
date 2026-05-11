from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


def evaluate_degree(xtrain, xtest, ytrain, ytest, degree: int) -> tuple[float, float]:
	poly = PolynomialFeatures(degree=degree)
	xtrain_poly = poly.fit_transform(xtrain)
	xtest_poly = poly.transform(xtest)

	model = LinearRegression()
	model.fit(xtrain_poly, ytrain)

	pred_train = model.predict(xtrain_poly)
	pred_test = model.predict(xtest_poly)

	r2_train = r2_score(ytrain, pred_train)
	r2_test = r2_score(ytest, pred_test)
	return r2_train, r2_test


housing = fetch_california_housing(as_frame=True)
data = housing.frame

x = data[["MedInc"]]
y = housing.target

xtrain, xtest, ytrain, ytest = train_test_split(
	x, y, test_size=0.2, random_state=42
)

results: list[tuple[int, float, float]] = []
for degree in (1, 2, 3):
	r2_train, r2_test = evaluate_degree(xtrain, xtest, ytrain, ytest, degree)
	results.append((degree, r2_train, r2_test))


print("Ступінь полінома | R² поїзд | Тест R²")
print("-" * 39)
for degree, r2_train, r2_test in results:
	print(f"{degree:^15} | {r2_train:>7.4f} | {r2_test:>7.4f}")
