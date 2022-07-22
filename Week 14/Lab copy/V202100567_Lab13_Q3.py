import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1,0,1])
y = np.zeros(x.shape)

'''(a) Complete the code above in order to add the vector v to each row of a matrix x.'''
for i in range (x.shape[0]):
    for j in range(x.shape[1]):
        (y[i,j]) = x[i,j] + v[j]

''' (b) The previous code works well; however when the matrix x is very large, computing an explicit
loop in Python could be slow. An alternative is to use NumPy. In this question, you are required
to used NumPy to compute y from x and v without explicit loops.'''

y = np.add(x, v)

