import matplotlib.pyplot as plt 
import pickle 
fig,ax=plt.subplots()
ax.plot([1,2,3,4],[11,22,33,44],label='ine1')
ax.set_title('simple plot')
ax.set_xlabel('y')
ax.set_ylabel('z')
ax.legend()
with open('plot.pkl','wb') as f:
    pickle.dump(fig,f)
with open('plot.pkl','rb') as f:
    fig=pickle.load(f)
plt.show()