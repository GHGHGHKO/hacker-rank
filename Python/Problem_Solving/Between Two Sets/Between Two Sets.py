#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def LCM(x, y):
    return x * y // gcd(x, y)

def GCDs(arr):
    while(True):
        if len(arr) == 1:
            return arr[0]
        
        else:
            arr.append(gcd(arr.pop(), arr.pop()))
        
def LCMs(arr):
    while(True):
        if len(arr) == 1:
            return arr[0]
        
        else:
            arr.append(LCM(arr.pop(), arr.pop()))

def getTotalX(a, b):
    # Write your code here
    
    # Greatest common factor
    # gcd(24, 36) = 12
    
    # Least common multiple
    # 2 * 6 // gcd(2, 6) = 6
    result = 0
    for i in range(1, GCDs(b)//LCMs(a)+1):
        if (GCDs(b) % (LCMs(a) * i)) == 0:
            result += 1
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
