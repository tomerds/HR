import math
import os
import random
import re
import sys

# # Complete the sherlockAndAnagrams function below.
# def sherlockAndAnagrams(s):
#     d = makeDict(s)
#     count = 0
#
#     for key in d:
#         for i in range(len(d[key])):
#             for j in range(i+1, len(d[key])):
#                 print(d[key][i], d[key][j])
#                 if d[key][i] == d[key][j]:
#                     count += 1
#
#     return count

def sherlockAndAnagrams(s):
    d = makeDict(s)
    count = 0

    print(d)

    for key, value in d.items():
        count += value*(value-1)/2

    return int(count)`

def makeDict(s):
    dictionary = {}
    substringslist = []
    for i in range(len(s)):
        substringslist.append(s[i])
        stringstore = s[i]
        for j in range(i+1, len(s)):
            stringstore += s[j]
            substringslist.append(''.join(sorted(stringstore)))

    # for i in range(len(substringslist)):
    #     substringslist[i] = ''.join(sorted(substringslist[i]))
    #     if len(substringslist[i]) not in dictionary:
    #         dictionary[len(substringslist[i])] = [substringslist[i]]
    #     else:
    #         dictionary[len(substringslist[i])].append(substringslist[i])

    for i in substringslist:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1

    return dictionary


print(sherlockAndAnagrams('cdcd'))