import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    lengthOfString = len(s)
    timesInto = n // lengthOfString
    leftOver = n % lengthOfString
    newString = s * timesInto

    listString = list(newString)
    newList = listString

    for i in range(leftOver):
        newList.append(listString[i])

    aCount = 0
    for i in range(len(newList)):
        if(newList[i] == 'a'):
            aCount += 1

    return aCount


def repeatedString2(s, n):
    aCount = s.count('a')
    lengthOfString = len(s)

    timesInto = n // lengthOfString
    leftOver = n % lengthOfString

    sList = list(s)

    if(leftOver != 0):
        aCount = aCount * timesInto
        for i in range(leftOver):
            if(sList[i] == 'a'):
                aCount += 1

    else:
        aCount = aCount * timesInto

    print(aCount)
    return aCount


repeatedString2('aba', 10)
