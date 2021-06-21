#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total_Cost = int((sum(bill) - bill[k]) / 2)
    if total_Cost != b:
        print (b - total_Cost)
    else:
        print ('Bon Appetit')

if __name__ == '__main__':
    nk = input().rstrip().split() # init arrays

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split())) # ate foods

    b = int(input().strip()) # brian charged

    bonAppetit(bill, k, b)
