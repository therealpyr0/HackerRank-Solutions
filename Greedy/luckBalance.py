# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N,K=sys.stdin.readline().split()
N=int(N)
K=int(K)
totalluck=0
impbuffer=[]
for i in xrange(N):
    l,t=sys.stdin.readline().split()
    l=int(l)
    t=int(t)
    if t==1:
        impbuffer.append(l)
    else:
        totalluck+=l
impbuffer.sort(reverse=True)
print totalluck+sum(impbuffer[:K])-sum(impbuffer[K:])

    