
import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.


def hourglassSum(arr):
    maxSum = 0

    for i in range(4):
        for j in range(4):

            top = sum(arr[i][j:j+3])

            middle = arr[i+1][j+1]

            bottom = sum(arr[i+2][j:j+3])

            hourglass = top + middle + bottom

            if(hourglass > maxSum):
                maxSum = hourglass

    return maxSum
