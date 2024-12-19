def first_double_peak(sequence):
    for i in range(len(sequence) - 2):
        if sequence[i+2] > sequence[i+3] and sequence[i+2] > sequence[i+4] and sequence[i+2] > sequence[i] and sequence[i+2] > sequence[i+1]:
            return i+2
    return -1
