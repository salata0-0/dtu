import numpy as np

def robust_values(x):
    robust = []
    mean = np.mean(x)
    std = np.std(x)

    for i in range(len(x)):
        if mean - std <= x[i] <= mean + std:
            robust.append(x[i])

    return robust