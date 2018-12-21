#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
h={}
overallmin=1000000000000000000
localmin=0
for i in xrange(n):
    if h.has_key(A[i]):
        h[A[i]].append(i)
        if len(h[A[i]])>1:
            localmin=h[A[i]][-1]-h[A[i]][-2]
            if localmin<overallmin:
                overallmin=localmin
    else:
        h[A[i]]=[]
        h[A[i]].append(i)
#print h
if overallmin==1000000000000000000:
    print "-1"
else:
    print overallmin
        