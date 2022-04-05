#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p_cnt = len(list(filter(lambda x: (x > 0), arr)))
    n_cnt = len(list(filter(lambda x: (x < 0), arr)))
    z_cnt = len(list(filter(lambda x: (x == 0), arr)))
    
    print(p_cnt / len(arr))
    print(n_cnt / len(arr))
    print(z_cnt / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
