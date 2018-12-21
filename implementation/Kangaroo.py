#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    if v1<=v2:
        return "NO"
    while 1:
        x1=x1+v1
        x2=x2+v2
        if x1==x2:
            return "YES"
        if x1>x2:
            return "NO"
    # Complete this function

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
