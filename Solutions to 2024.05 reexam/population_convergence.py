def population_convergence(N, r):
    years  = 0

    while N >= 10.1 or N <= 9.9:
        N = N + r * (1 - N / 10) * N
        years += 1

    return years