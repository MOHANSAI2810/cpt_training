import matplotlib.pyplot as plt 
import numpy as np 
x=[1,2,3,4,5]
y=[10,20,30,40,50]
z=[60,70,80,90,100]
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.subplot(2, 2, 2)
plt.plot(x, z)
plt.subplot(2, 2, 3)
plt.plot(y, z)
plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.show()