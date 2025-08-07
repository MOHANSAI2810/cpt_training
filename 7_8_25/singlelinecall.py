import matplotlib.pyplot as plt 
import numpy as np 
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,'b-',x,y2,'r--')
plt.legend()
plt.show()