import itertools
from collections import Counter
data=input("Enter the characters")
permute=list(itertools.permutations(data))
c=0
e=[]
for i in permute:
    d=' '.join(i)
    
    c+=1
    
    e.append(d)
print(Counter(''.join(e)))
print(c)