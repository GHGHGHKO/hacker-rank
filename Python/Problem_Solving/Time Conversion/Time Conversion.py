#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == 'PM':
        if int(s[0:2]) >= 12:
            #print('translate time ' + s[:-2])
            return s[:-2]
        else:
            #print('translate time ' + str(int(s[0:2]) + 12) + s[2:-2])
            return (str(int(s[0:2]) + 12) + s[2:-2])
            
    else:
        if int(s[0:2]) >= 12:
            #print('translate time ' + str(int(s[0:2]) - 12).zfill(2) + s[2:-2])
            return (str(int(s[0:2]) - 12).zfill(2) + s[2:-2])
        else:
            #print('translate time ' + s[:-2])
            return (s[:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
