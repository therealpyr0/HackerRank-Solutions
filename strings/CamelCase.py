#!/bin/python

import sys


s = raw_input().strip()
l=len(s)
c=0
for i in xrange(1,l):
    if s[i].isupper():
        c+=1
print c+1
        
