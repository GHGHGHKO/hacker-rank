#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result_list = []
    # Write your code here
    for grade in grades:
        if abs((grade % 5) - 5) < 3:
            if (grade + abs((grade % 5) - 5)) < 40:
                result_list.append(grade)
            else:
                result_list.append(grade + abs((grade % 5) - 5))
                
        else:
            result_list.append(grade)
                
    return result_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
