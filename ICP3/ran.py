import numpy as np
x = np.random.uniform(1,high=20, size=20)
print(x)
a = x.reshape(4, 5)
print(a)
row_maxes = np.amax(a, axis=1)
#print(np.where(np.argmax(a, axis=1), 0, a))
print(row_maxes)
#max_index_row = np.argmax(a, axis=1)
#print(max_index_row)
#result = np.where(max_index_row, a, 0)   a == np.amax(a)

b = np.where(a == row_maxes.reshape(-1,1),0,a)
print(b)
