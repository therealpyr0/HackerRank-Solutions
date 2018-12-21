#!/bin/python

import sys


g = int(raw_input().strip())
count=0
m=0
for a0 in xrange(g):
    n = int(raw_input().strip())
    l=[int(i) for i in sys.stdin.readline().split()]
    count=0
    m=0
    for num in l:
        if num>m:
            count+=1
            m=num
    if count%2==0:
        print "ANDY"
    else:
        print "BOB"

