#!/bin/python

import sys

def containshr(s):
    s1="hackerrank"
    l1=len(s1)
    l=len(s)
    count=0
    for i in xrange(l):
        if s[i]==s1[count]:
            count+=1
        if count==l1-1:
            return "YES"
    if count==l1-1:
        pass
    else:
        return "NO"
    pass


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    print containshr(s)
    # your code goes here
