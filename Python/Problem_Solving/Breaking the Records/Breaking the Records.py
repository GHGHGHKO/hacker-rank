#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest_Score = scores[0]
    lowest_Score = scores[0]
    highest_Point = 0
    lowest_Point = 0
    
    for score in scores:
        if score < lowest_Score:
            lowest_Score = score
            lowest_Point += 1
        elif score > highest_Score:
            highest_Score = score
            highest_Point += 1
        else:
            pass
    return highest_Point, lowest_Point
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
