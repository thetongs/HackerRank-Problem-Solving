#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    high_cnt = 0
    low_cnt = 0

    present_score_h = scores[0]
    present_score_l = scores[0]
    for score in scores[1:]:
        if(score > present_score_h):
            present_score_h = score
            high_cnt = high_cnt + 1

        if(score < present_score_l):
            present_score_l = score
            low_cnt = low_cnt + 1
    
    return [high_cnt, low_cnt]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
