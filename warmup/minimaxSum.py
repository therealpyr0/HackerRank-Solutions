#!/bin/python

import sys


#a,b,c,d,e = raw_input().strip().split(' ')
#a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
l=[int(i) for i in sys.stdin.readline().split(" ")]
s=sum(l)
#l=l.sort()
print s-max(l),s-min(l)