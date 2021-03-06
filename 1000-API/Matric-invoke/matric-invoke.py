import os
import re
import sys
import numpy as np
def matric_invoke(inFile, outFile):
    f = open(inFile, "r")
    count = sum(1 for line in open('API-invoke.txt'))
    arr = []
    for line in f:
        arr.append(line)
    A = np.eye(count,dtype=int)
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][0:arr[x].find('{')] == arr[y][0:arr[y].find('{')]:
                A[x][y] =1
    for x in range(len(arr)):
        for y in range(len(arr)):
            outFile.write(str(A[x][y]) + "\t")
        outFile.write("\n")

pass
inFile = "API-invoke.txt"
resultFile = open("matric-invoke.txt", "w")

matric_invoke(inFile, resultFile)

resultFile.close()

print('done!')
