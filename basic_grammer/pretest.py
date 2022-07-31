import numpy as np
array = np.arange(8)

# 1
array = array.reshape(2,4)

print(array)


# 2
A = np.random.randint(0,100,[1,10])
B = np.random.randint(0,100,[10,1])

print(A+B)