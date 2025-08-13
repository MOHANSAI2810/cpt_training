import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt  
data={
    'hours':[1,2,3,4,5,6,7,8],
    'marks':[21,31,54,21,56,21,43,56],
    'pass':[0,1,1,0,1,1,0,1]
}
df=pd.DataFrame(data)
sns.set_style('whitegrid')
sns.histplot(data=df,x='hours',y='marks',palette='viridis')
plt.show()