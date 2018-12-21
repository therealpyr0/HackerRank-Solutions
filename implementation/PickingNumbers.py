#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
countarr=[0 for i in range(108)]
for i in a:
    countarr[i-1]+=1
#print countarr
count=0
for i in range(n-1):
    count=max(count,countarr[i]+countarr[i+1])
print count
    

