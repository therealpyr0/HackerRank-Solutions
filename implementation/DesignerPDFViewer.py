#!/bin/python

import sys

m=0
h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()
adict={}
c=0
for i in xrange(ord('a'),ord('z')+1):
    adict[chr(i)]=h[c]
    c+=1
for i in xrange(len(word)):
    if adict[word[i]]>m:
        m=adict[word[i]]
print len(word)*m
    
