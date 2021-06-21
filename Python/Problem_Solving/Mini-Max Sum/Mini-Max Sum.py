#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sumArr = sum(arr)
    
    minArr = min(arr)
    maxArr = max(arr)
    
    print(sumArr - maxArr, sumArr - minArr)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
