def special_occurrence(sequence):
    for i in range (len(sequence) - 2):
        if sequence[i] == 5 and ((sequence[i+1] == 7 and sequence[i+2] != 7) or (sequence[i+1] != 7 and sequence[i+2] == 7)):
            return i
    return -1