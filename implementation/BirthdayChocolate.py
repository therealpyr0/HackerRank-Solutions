#!/bin/python

import sys

def solve(n, s, d, m):
    max=0
    s1=sum(s[0:m])
    j=0
    #max=s1
    count=0
    if s1==d:
        count+=1
    for i in xrange(m,n):
        s1=s1-s[j]+s[i]
        j=j+1
        if s1==d:
            count+=1
    return count
        
    # Complete this function

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
