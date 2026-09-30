#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    
    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]
        
        idx = (x ^ lastAnswer) % n
        
        if query_type == 1:
            arr[idx].append(y)
        elif query_type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
            
    return answers

if __name__ == '__main__':
    # Read the first line containing n and q
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []

    # Read each query row
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    # Call your function
    result = dynamicArray(n, queries)

    # Print the result matching the expected output format
    print('\n'.join(map(str, result)))
