#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for vertical in range(n, 0, -1):
        print (' ' * (vertical-1) + '#' * (n-(vertical-1)))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
