

import math
import os
import random
import re
import sys


# The function accepts INTEGER_ARRAY a as parameter.


def countSwaps(a):
    c = 0
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                c = c+1
    print('Array is sorted in',c,'swaps.') 
    print('First Element:',a[0])
    print('Last Element:',a[len(a)-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
