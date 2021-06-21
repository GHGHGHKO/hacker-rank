#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum_1 = 0
    sum_2 = 0
    for fst, snd in zip(range(0, len(arr[0])), range(len(arr[0])-1, -1, -1)):
        sum_1 += arr[fst][fst]
        sum_2 += arr[fst][snd]
    
            
    
    return abs(sum_1 - sum_2)
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
   