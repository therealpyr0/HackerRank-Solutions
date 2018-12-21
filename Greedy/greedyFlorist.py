#!/bin/python

import sys

def getMinimumCost(n, k, c):
    count=0
    factor=0
    totalcost=0
    c.sort(reverse=True)
    l=len(c)
    for i in xrange(l):
        cost=(factor+1)*c[i]
        #print "cost : ",cost
        totalcost+=cost
        count+=1
        if count%k==0 and count!=0:
            factor+=1
    return totalcost
    # Complete this function

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
c = map(int, raw_input().strip().split(' '))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)
