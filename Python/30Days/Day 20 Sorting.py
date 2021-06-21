#!/bin/python3

import sys

n = int(input().strip()) # init array
a = list(map(int, input().strip().split(' '))) # insert numbers ex, 4 3 1 2
# Write Your Code Here
result = 0

for i in range(n - 1, 0, -1):
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            result += 1
            
print('Array is sorted in ' + str(result) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[-1]))