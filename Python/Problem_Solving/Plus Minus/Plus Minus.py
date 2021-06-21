#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
            
    if positive != 0:
        print (format((positive / n), ".6f"))
    else:
        print (format(0, ".6f"))
        
    if negative != 0:
        print (format((negative / n), ".6f"))
    else:
        print (format(0, ".6f"))
        
    if zero != 0:
        print (format((zero / n), ".6f"))
    else:
        print (format(0, ".6f"))
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
