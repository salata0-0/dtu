def name_frequency(names):
    frequency = {}
    first = [name.split()[0] for name in names]

    for name in first:
        if name in frequency:
            frequency[name] += 1
        else:
            frequency[name] = 1

    return frequency