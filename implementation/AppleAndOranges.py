#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apples = map(int,raw_input().strip().split(' '))
oranges = map(int,raw_input().strip().split(' '))
applecount=0
orangecount=0
for apple in apples:
    if apple+a>=s and apple+a<=t:
        applecount+=1

for orange in oranges:
    if orange+b>=s and orange+b<=t:
        orangecount+=1
print applecount
print orangecount