#!/bin/python

import sys
buffer=""
h=set()
s=0
s = raw_input().strip()
l=len(s)
prev=""
val=0
buff=""
for i in xrange(0,l):
    if s[i]==prev:
     #   print "same"
        buff+=s[i]
        val=(ord(s[i])-ord('a')+1)*(len(buff)+1)
        h.add(val)
    else:
    #    print "changed"
        val=ord(s[i])-ord('a')+1
        prev=s[i]
        buff=""
        h.add(val)
   # print h
    pass
#print h
n = int(raw_input().strip())
#print h
for a0 in xrange(n):
    x = int(raw_input().strip())
    if x in h:
        print "Yes"
    else:
        print "No"
    # your code goes here
