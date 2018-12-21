#!/bin/python

import sys

def stringConstruction(s):
    l=len(s)
    h={}
    count=0
    for i in xrange(l):
        if h.has_key(s[i]):
            pass
        else:
            h[s[i]]=0
            count+=1
    return count
    # Complete this function

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        result = stringConstruction(s)
        print result

