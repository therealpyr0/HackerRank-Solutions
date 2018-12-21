#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
l=len(s)
q=n/l
r=n%l
tillr=0
total=0
for i in xrange(l):
    if s[i]=='a':
        if i<r:
            tillr+=1
        total+=1
print (total*q)+(tillr)
        
        
    
