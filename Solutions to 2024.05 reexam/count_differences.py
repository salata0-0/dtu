import os

def count_differences(filename1, filename2):
    count = 0

    with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
        res1 = file1.readline().strip().split(',')
        res2 = file2.readline().strip().split(',')

    if len(res1) != len(res2):
        return -1
    
    for i in range(len(res1)):
        if res1[i] != res2[i]:
            count += 1

    return count