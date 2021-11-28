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
    # Store the array length into the variable len.
    length = len(arr);
    # Initialize the postiveCount, negativeCount, and
    # zeroCountby 0 which will count the total number
    # of positive, negative and zero elements
    positiveCount = 0;
    negativeCount = 0;
    zeroCount = 0;
    # Traverse the array and count the total number of
    # positive, negative, and zero elements.
    for i in range(length):
        if (arr[i] > 0):
            positiveCount += 1;
        elif(arr[i] < 0):
            negativeCount += 1;
        elif(arr[i] == 0):
            zeroCount += 1;
         
    # Print the ratio of positive,
    # negative, and zero elements
    # in the array up to four decimal places.
    print("{0:.6f}".format((positiveCount / length)));
    print("%1.6f "%(negativeCount / length));
    print("%1.6f "%(zeroCount / length));
    print();
 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
