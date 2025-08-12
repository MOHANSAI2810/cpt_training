from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
np.random.seed(42)
x,y=make_regression(n_features=100,n_samples=10,noise=15)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)
lasso=Lasso(0.1)
lasso.fit(x_train,y_train)
y_pred=lasso.predict(x_test)
print(lasso.coef_)
print(mean_squared_error(y_test,y_pred))
  