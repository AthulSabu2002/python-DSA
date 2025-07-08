#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def migratoryBirds(arr):
    arr.sort()
    temp = {}
    
    for x in arr:
        if x in temp:
            temp[x] += 1
        else:
            temp[x] = 1
    
    max_count = 0 
    
    for bird, count in temp.items():
        if count > max_count:
            max_count = count
            max_bird = bird
        elif count == max_count:
            max_bird = min(max_bird, bird)
    
    return max_bird

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
