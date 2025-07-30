import numpy as np
a = np.array([0, 30, 45, 60])
b = np.array([5, 6, 7, 8])
print(a+b, a-b, a*b, a/b)
print(np.sin(a))

c = np.arange(1, 10)
d = c.reshape(3, 3)
print(d)

linear = d.reshape(-1)
print(linear)

print("Greater than 5", linear[linear > 5])
print("Less than 5", linear[linear < 5])

print("Random numbers between 0 to 3", np.random.rand(3))
print("Random integer \n", np.random.randint(1, 100, (2, 3)))
