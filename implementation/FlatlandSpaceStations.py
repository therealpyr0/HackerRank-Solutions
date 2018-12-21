#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))
c.sort()
pointer=0
globalmax=0
if n==m:
    print "0"
    
else:
    for i in xrange(n):
        if i==c[pointer]:
            pass
        else:
            if (pointer+1)<=(m-1):
                diff2=abs(i-c[pointer+1])
                diff1=abs(i-c[pointer])
                if diff1>diff2:
                    diff=diff2
                    pointer+=1
                else:
                    #print "pointer increased ",pointer
                    diff=diff1
                    #pointer+=1
            else:
                diff=abs(i-c[pointer])
            if diff>globalmax:
                #print "globalmax changed"
                globalmax=diff
    print globalmax
                
            
        
