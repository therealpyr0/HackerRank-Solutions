#!/bin/python

import sys
c=0
n = int(raw_input().strip())
b = list(raw_input().strip())
l=len(b)
check=1
blist=list(b)
while 1:
    check=1
    for i in xrange(l-2):
        if blist[i]=="0" and blist[i+1]=="1" and blist[i+2]=="0":
            c=c+1
            blist[i+2]="1"
            #print blist
            #print "asd"
            check=0
    if check:
        break
print c