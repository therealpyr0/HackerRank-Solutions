# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
h={}
N=int(sys.stdin.readline())
for n in xrange(N):
    t,d=[int(i) for i in sys.stdin.readline().split()]
    a=t+d
    if h.has_key(a):
        h[a].append(n)
    else:
        h[a]=[]
        h[a].append(n)
key=h.keys()
key.sort()
for k in key:
    for x in h[k]:
        print x+1,
        