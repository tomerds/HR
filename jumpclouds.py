
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):

    cloud = 0
    cloudsarray = [0]
    while cloud < len(c)-1:
        print(cloud)
        # if(cloud + 2 < len(c)):
        #     if(c[cloud+2] == 0):
        #         cloud += 2
        if(cloud+2 < len(c) and c[cloud+2] != 1):
            cloud += 2
            cloudsarray.append(cloud)

        elif(cloud+1 < len(c) and c[cloud+1] != 1):
            cloud += 1
            cloudsarray.append(cloud)

    return len(cloudsarray)-1


print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))
