import pickle
class student:
    def __init__(self,name,age):
        self.name = name 
        self.age=age 
    def hi(self):
        return f"Hello, my name is {self.name} and I am {self.age}"
s=student('Mohan',19)
with open('student.pkl','wb') as f:
    pickle.dump(s,f)
with open('student.pkl','rb') as f:
    s=pickle.load(f)
print(s.name)
print(s.hi())