from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

housing = fetch_california_housing(as_frame=True)
data = housing.frame

x = data[["MedInc"]]
y = housing.target

poly = PolynomialFeatures(degree=2)
xpoly = poly.fit_transform(x)

xtrain, xtest, ytrain, ytest = train_test_split(
    xpoly, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(xtrain, ytrain)

pred = model.predict(xtest)
r2 = r2_score(ytest, pred)

print(f"R2 test: {r2:.4f}")