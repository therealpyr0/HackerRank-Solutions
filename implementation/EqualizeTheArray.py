# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n=int(sys.stdin.readline())
arr=[int(i) for i in sys.stdin.readline().split()]
h={}
for i in arr:
    if h.has_key(i):
        h[i]+=1
    else:
        h[i]=1
m=0
for i in h:
    if h[i]>m:
        m=h[i]
print n-m