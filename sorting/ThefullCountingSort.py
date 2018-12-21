# Enter your code here. Read input from STDIN. Print output to STDOUT
h={}
import sys
n=int(sys.stdin.readline())
arr=[]
for i in xrange(n):
    a,s=sys.stdin.readline().strip().split(" ")
    a=int(a)
    #arr.append(a)
    if h.has_key(a):
        if i<(n/2):
            h[a].append("-")
        else:
            h[a].append(s)
    else:
        h[a]=[]
        if i<n/2:
            h[a].append("-")
        else:
            h[a].append(s)
arr=h.keys()
arr.sort()
for i in arr:
    for s in h[i]:
        print s,