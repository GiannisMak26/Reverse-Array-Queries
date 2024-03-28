#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'performOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY operations
#

def reverseSubArray(arr, start, end):
    arr[start:end+1] = arr[start:end+1][::-1]
    return arr

def performOperations(arr, operations):
    answerarray = arr[:]
    x = len(operations)
    for i in range(x):
        answerarray = reverseSubArray(answerarray, operations[i][0], operations[i][1])
    return answerarray
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    operations_rows = int(input().strip())
    operations_columns = int(input().strip())

    operations = []

    for _ in range(operations_rows):
        operations.append(list(map(int, input().rstrip().split())))

    result = performOperations(arr, operations)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()