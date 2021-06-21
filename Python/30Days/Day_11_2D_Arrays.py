#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    result = -100000
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
       
    for ver in range(0, 4):
        for row in range(0, 4):
            a = arr[0 + ver][0 + row]
            b = arr[0 + ver][1 + row]
            c = arr[0 + ver][2 + row]
            d = arr[1 + ver][1 + row]
            e = arr[2 + ver][0 + row]
            f = arr[2 + ver][1 + row]
            g = arr[2 + ver][2 + row]
            
            if (a, b, c, d, e, f, g) != 0:
                if result < sum([a, b, c, d, e, f, g]):
                    result = sum([a, b, c, d, e, f, g])          
            
    print(result)