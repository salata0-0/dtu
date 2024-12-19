def event_probability(T, n):
    P = 1 - (1 - 1/T) ** n
    return P