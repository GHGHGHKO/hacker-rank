#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    result = 0
    counted = 0
    for gua in range(1, 6):
        print(gua, arr.count(gua), result)
        if arr.count(gua) > counted:
            counted = arr.count(gua)
            result = gua
            print('result', result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
