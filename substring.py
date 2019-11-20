#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    D1 = makeDictionary(s1)
    D2 = makeDictionary(s2)

    r = 'NO'

    for key in D1:
        if key in D2:
            r = "YES"

    return r



def makeDictionary(string):

    dictionary = {}

    for i in range(len(string)):
        if string[i] not in dictionary:
            dictionary[string[i]] = 1
        else:
            dictionary[string[i]] += 1

    return dictionary

print(twoStrings('hello','goodbye'))

