#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    lowerMax = 122
    lowerMin = 97
    
    upperMax = 90
    upperMin = 65

    sList = list(s)

    for char, i in zip(sList, range(0, len(s))):
        if ord(char) >= lowerMin and ord(char) <= lowerMax:
            pre = ord(char) + k
            if pre > lowerMax:
                while pre > lowerMax:
                    pre = pre % lowerMax + lowerMin - 1

            sList[i] = chr(pre)

        elif ord(char) >= upperMin and ord(char) <= upperMax:
            pre = ord(char) + k
            if pre > upperMax:
                while pre > upperMax:
                    pre = pre % upperMax + upperMin - 1

            sList[i] = chr(pre)
            
    result = "".join(sList)     
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
