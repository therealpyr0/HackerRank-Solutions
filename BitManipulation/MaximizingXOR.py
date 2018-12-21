#!/bin/python

# Complete the function below.

    

l = int(raw_input())


r = int(raw_input())
m=0
a=0
for i in xrange(l,r+1):
    for j in xrange(i,r+1):
        a=i^j
        if a>=m:
            m=a
        
print(m)

