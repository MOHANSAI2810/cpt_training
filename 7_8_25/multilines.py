import matplotlib.pyplot as plt 
import numpy as np 
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)

plt.plot(x,y1,label='sin(x)',color='b')
plt.plot(x,y2,label='cos(x)',color='g')
plt.plot(x,y3,label='tan(x)',color='r')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Multiple lines in a plot')
plt.legend(title='menu')
plt.grid()
plt.show()