#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
h={}
for i in c:
    if h.has_key(i):
        h[i]+=1
    else:
        h[i]=1
total=0
for i in h:
    total+=h[i]/2
print total
