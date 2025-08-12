from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.datasets import make_regression
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(42)
x, y = make_regression(n_samples=1000, n_features=10, noise=15)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)
ElasticNet=ElasticNet(alpha=0.1)
ElasticNet.fit(x_train,y_train)
y_pred=ElasticNet.predict(x_test)
print(ElasticNet.coef_)
print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred)*100)
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111,projection='3d')
ax.scatter(x_test[:,0],x_test[:,1],y_test,c='blue')
ax.scatter(x_test[:,0],x_test[:,1],y_pred,c='r')
plt.show()