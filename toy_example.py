import numpy as np 

#1*3 2*3

x = [1,2]
y = [[1,2],[1,2]]

mx = np.matrix(x)
my = np.matrix(y)   

print(y)
print(x)
print(mx * my)