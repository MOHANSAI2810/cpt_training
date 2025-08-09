import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([
    [50, 2.0, 3, 150],
    [30, 1.8, 2, 140],
    [70, 2.5, 5, 160],
    [20, 1.6, 1, 130],
    [90, 3.0, 6, 200],
    [60, 2.2, 4, 155]
])

y = np.array([15, 18, 12, 22, 10, 14])

model = LinearRegression()
model.fit(X, y)

new_car = np.array([[40, 2.0, 3, 145]])
predicted_price = model.predict(new_car)
print(f"Predicted price for the new car: {predicted_price[0]:.2f}k")

accuracy = model.score(X, y)
print(f"Model R^2 score: {accuracy:.2f}")

predicted = model.predict(X)
plt.scatter(y, predicted)
plt.xlabel("Actual Price (k)")
plt.ylabel("Predicted Price (k)")
plt.title("Actual vs Predicted Car Prices")
plt.plot([min(y), max(y)], [min(y), max(y)], 'r--')
plt.show()
