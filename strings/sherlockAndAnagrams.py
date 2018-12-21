#!/bin/python

import sys
def sherlockAndAnagrams(s):
    h={}
    count=0
    # Complete this function
    l=len(s)
    for i in xrange(l):
        for j in xrange(i,l):
            s1=''.join(sorted(s[i:j+1]))
            ha=hash(s1)
            if h.has_key(ha):
                h[ha]+=1
                #print s1," : same"
                #print "same : ",s[i:j+1]
            else:
                h[ha]=1
    #print h
    for key in h:
        if h[key]==1:
            pass
        else:
            count+=((h[key]*(h[key]-1)))/2
    return count
            
            
            

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = sherlockAndAnagrams(s)
    print(result)

