#!/bin/python

import sys

def getdigitsum(num):
    n=num
    s=0
    for i in range(len(num)):
        s+=int(num[i])
    if s>=10:
        return getdigitsum(str(s))
    else:
        return s

def superDigit(n, k):
    # Complete this function
    x=getdigitsum(n)
    x=x*k
    return getdigitsum(str(x))

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = superDigit(n, k)
    print result
