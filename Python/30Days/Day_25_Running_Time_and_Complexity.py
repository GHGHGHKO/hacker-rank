# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def is_Prime(num):
    if num <= 1:
        return False
    
    sqrt_Num = int(math.sqrt(num))
    
    for i in range(2, sqrt_Num + 1): # 2 to sqrt_Num
        if num % i == 0: # num % range
            return False # Not prime
    return True # Prime

T = int(input())

for _ in range(T):
    n = int(input())
    if is_Prime(n) == False:
        print ('Not prime')
    else:
        print('Prime')
    