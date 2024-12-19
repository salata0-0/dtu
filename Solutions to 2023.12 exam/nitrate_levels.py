import os

def nitrate_levels(filename):
    categories = [0, 0, 0, 0, 0]

    with open(filename, 'r') as file:
        for line in file:
            value = float(line.strip())
            if value <= 4.0:
                categories[0] += 1
            elif value <= 9.0:
                categories[1] += 1
            elif value < 40.0:
                categories[2] += 1
            elif value < 50.0:
                categories[3] += 1
            else:
                categories[4] += 1
                
    return tuple(categories)