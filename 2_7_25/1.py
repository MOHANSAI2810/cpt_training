import json
a=input("Enter the name")
b=int(input("Enter the no.of subjects"))
d={}
for i in range(b):
    c=int(input("Enter the individual marks"))
    d[i]=c
with open('user.json','w') as f:
    json.dump(d,f)
with open('user.json','r') as f:
    loaded=json.load(f)
    print(loaded)