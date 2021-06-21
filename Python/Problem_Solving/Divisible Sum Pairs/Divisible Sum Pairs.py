#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
from math import gcd

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    permute = permutations(ar, 2)
    result = 0
    
    for i in permute:
        if gcd(sum(i), k) == k:
            result += 1
            
    return int(result / 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0]) # n -> num of array

    k = int(nk[1]) # x % k == 0

    ar = list(map(int, input().rstrip().split())) # insert array

    result = divisibleSumPairs(n, k, ar)
    
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
