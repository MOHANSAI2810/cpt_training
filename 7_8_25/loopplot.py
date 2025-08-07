import matplotlib.pyplot as plt 
import numpy as np 
x=np.linspace(0,10,100)
y=[(np.sin(x),'sin(x)','red'),(np.cos(x),'cos(x)','blue'),(np.tan(x),'tan(x)','green')]
for values, label, color in y:
    plt.plot(x, values, label=label, color=color)
plt.grid()
plt.legend(title='menu')
plt.xlabel("x")
plt.ylabel('y')
plt.title('This is a basic plot')
plt.show()