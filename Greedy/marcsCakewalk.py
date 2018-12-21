#!/bin/python

import sys


n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))
calories.sort(reverse=True)
s=0
cakes=0
for i in calories:
    s=s+(i*(pow(2,cakes)))
    cakes+=1
print s
# your code goes here
