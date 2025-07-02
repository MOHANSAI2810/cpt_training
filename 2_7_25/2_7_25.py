# import json
# name=input("Enter the name")
# age=int(input("Enter the age"))
# data={'name':name,'age':age}
# string=json.dumps(data)
# print(data)

import json

name=input("Enter the name")
age=int(input("Enter the age"))
user={'name':name,'age':age}
with open('user.json','w') as f:
    json.dump(user,f)
print("Data written to json folder")

with open('user.json','r') as f:
    loaded=json.load(f)
    print(loaded)