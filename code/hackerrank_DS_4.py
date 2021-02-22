# -*- coding: utf-8 -*-
"""
Created on 19/01/2021 16:11

@author: Akhil

 The function is expected to return an INTEGER_ARRAY.
 The function accepts following parameters:
  1. INTEGER d
  2. INTEGER_ARRAY arr
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def rotateLeft(d, arr):
    temp = []
    for i in range(len(arr)):
        if i+d >= len(arr):
            temp.append(arr[i + d - len(arr)])
        else:
            temp.append(arr[i + d])

    # print(temp)
    return temp


def rotation():
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
    return result


if __name__ == '__main__':

    print(rotation())
