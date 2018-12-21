#!/bin/python

import sys
c=0


s = raw_input().strip()
for i in xrange(0,len(s),3):
    if s[i]=="S":
        pass
    else:
        c+=1
    if s[i+1]=="O":
        pass
    else:
        c+=1
    if s[i+2]=="S":
        pass
    else:
        c+=1
print c
