# Problem: https://www.hackerrank.com/challenges/python-sort-sort/

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    def sorting_func(item):
        return item[k]


arr.sort(key=sorting_func)

for li in arr:
    print(" ".join(list(map(str, li))))
