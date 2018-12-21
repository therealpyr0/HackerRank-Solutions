#!/bin/python

import sys
h={}
h1={}

def isValid(s):
    S=set()
    l=len(s)
    for i in xrange(l):
        if h.has_key(s[i]):
            h[s[i]]+=1
        else:
            h[s[i]]=1
    for key in h:
        if h1.has_key(h[key]):
            h1[h[key]]+=1
            pass
        else:
            h1[h[key]]=1
    for key in h:
        S.add(h[key])
    S=list(S)
    #print S
    if len(S)>2:
        return "NO"
    if len(S)==1:
        return "YES"
    if len(S)==2:
        if h.values().count(S[0])==1 or h.values().count(S[1])==1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
    # Complete this function

s = raw_input().strip()
result = isValid(s)
print(result)
