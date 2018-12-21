#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
c=0
for i in xrange(n):
    for j in xrange(i+1,n):
        if (a[i]+a[j])%k==0:
            c+=1
print c
