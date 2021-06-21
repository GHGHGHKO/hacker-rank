#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    reverse_list = []
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    for i in range(0, n):
        reverse_list.append(arr.pop())

    print(str(reverse_list)[1:-1].replace(',', ''))