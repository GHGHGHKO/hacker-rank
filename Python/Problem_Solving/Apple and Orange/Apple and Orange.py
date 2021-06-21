#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # s, t = house
    # a = apple tree
    # b = orange tree
    # m = num of apples
    # n = num of oranges
    
    harvested_Apples = 0
    harvested_Oranges = 0
    
    for apple in apples:
        if ((a + apple) >= s) and ((a + apple) <= t):
            harvested_Apples += 1
            
    for orange in oranges:
        if ((b + orange) >= s) and ((b + orange) <= t):
            harvested_Oranges += 1
    
    print (harvested_Apples)
    print (harvested_Oranges)
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
