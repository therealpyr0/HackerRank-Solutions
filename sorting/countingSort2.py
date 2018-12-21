# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n=int(sys.stdin.readline())
ar=[int(i) for i in sys.stdin.readline().split()]
adict={}
for i in ar:
    if adict.has_key(i):
        adict[i]=adict[i]+1
    else:
        adict[i]=1
for i in xrange(100):
    if adict.has_key(i):
        for j in xrange(adict[i]):
            print i,
