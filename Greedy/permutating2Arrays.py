# Enter your code here. Read input from STDIN. Print output to STDOUT

def permute(n,k,a,b):
    a.sort()
    b.sort(reverse=True)
    for i in xrange(n):
        if a[i]+b[i]<k:
            return "NO"
    return "YES"
    pass

import sys
Q=int(sys.stdin.readline())
for q in xrange(Q):
    n,k=sys.stdin.readline().split(" ")
    n=int(n)
    k=int(k)
    a=[int(i) for i in sys.stdin.readline().split(" ")]
    b=[int(i) for i in sys.stdin.readline().split(" ")]
    print permute(n,k,a,b)