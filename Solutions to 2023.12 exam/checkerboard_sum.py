import numpy as np

def checkerboard_sum(A):
    sum = 0

    for j in range(np.size(A,1)):
        if j % 2 == 0:
            sum += np.sum(A[::2,j])
        else:
            sum += np.sum(A[1::2,j])

    return sum