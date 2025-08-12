import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(42)
x,y=make_regression(n_samples=100,n_features=10,noise=10)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
ridge=Ridge(0.1)
ridge.fit(x_train,y_train)
y_pred=ridge.predict(x_test)
print(ridge.coef_)
print(mean_squared_error(y_test,y_pred))
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111,projection='3d')
ax.scatter(x_test[:,0],x_test[:,1],y_test,color='blue',label='Testing data')
ax.scatter(x_test[:,0],x_test[:,1],y_pred,color='red',label='predicting data')
ax.legend(title='scale')
ax.set_xlabel('feature 1')
ax.set_ylabel('feature 2')
ax.set_zlabel('target')
ax.set_title('Predicton using 3d plot')
plt.show()

# https://www.linkedin.com/posts/being-zero_registration-for-bzcl-25-activity-7360894230187139072-pzo/