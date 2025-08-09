import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([2, 4, 6, 4, 5])

model = LinearRegression()
model.fit(hours, marks)
model.predict([[6]])
plt.scatter(hours, marks, label='original data', color='blue')
plt.plot(hours, model.predict(hours), label='fitted line', color='red')
plt.show()
accuracy = model.score(hours, marks)
print(accuracy)
