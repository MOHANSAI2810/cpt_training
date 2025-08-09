import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
np.random.seed(42)
x = np.random.rand(100)*10
y = 3*x+5+np.random.rand(100)*2
m, c = np.polyfit(x, y, 1)
print(f"y={m:.2f}x+{c:.2f}")
print(f'Intercept(c):{c:.2f}')
newx = 9
print(f'Predicted y for x={newx:.2f}: {m*newx+c:.2f}')
plt.scatter(x, y, color='blue', alpha=0.6)
plt.plot(x, m*x+c, color='red')
plt.show()
