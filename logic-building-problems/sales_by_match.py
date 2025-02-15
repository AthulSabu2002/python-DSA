#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    count = 0
    dict = {}
    
    for num in ar:
        if num in dict:
            dict[num] +=1
        else:
            dict[num] = 1
    
    for c in dict:
        count += dict[c]//2
    
    return count

if __name__ == '__main__':
    # n = int(input().strip())
    # ar = list(map(int, input().rstrip().split()))
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)
    print("result: ", result)
    
    
# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.