import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
x = np.array([[1,2], [3,4], [5,6], [7,8]])
y = np.array([0, 0, 1, 1])
new_point = np.array([[4,4]])
scaler = StandardScaler()
x_scale = scaler.fit_transform(x)
scalednewpoint = scaler.transform(new_point)
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_scale, y)
prediction = knn.predict(scalednewpoint)
print('Predicted class:', prediction[0])
h = 0.02
x_min, x_max = x_scale[:, 0].min() - 1, x_scale[:, 0].max() + 1
y_min, y_max = x_scale[:, 1].min() - 1, x_scale[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(x_scale[:, 0], x_scale[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolor='k', s=100, label='Training points')
plt.scatter(scalednewpoint[:, 0], scalednewpoint[:, 1], c='green', edgecolor='k', s=150, marker='*', label='New point')
plt.legend()
plt.title(f'KNN Decision Boundary (k={k})')
plt.xlabel('Feature 1 (scaled)')
plt.ylabel('Feature 2 (scaled)')
plt.show()
