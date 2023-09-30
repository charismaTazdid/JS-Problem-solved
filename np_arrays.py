# Problem: https://www.hackerrank.com/challenges/np-arrays/

import numpy

def arrays(arr):
    arr.reverse()
    b = numpy.array(arr, float)
    return b


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
