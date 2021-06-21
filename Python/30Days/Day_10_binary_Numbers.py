#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    cnt = 0
    result = 0
    binary = bin(n)[2:]
    for_cnt = 0
    
    for i in binary:
        for_cnt += 1
        if i == str(1):
            cnt += 1
            
        else:
            if result < cnt:
                result = cnt
                cnt = 0
                
            else:
                cnt = 0
                
        if (for_cnt == len(binary)) and (cnt > result): # End for
            result = cnt
                
    print(result)
