# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n,k,q=[int(i) for i in sys.stdin.readline().split()]
ar=[int(i) for i in sys.stdin.readline().split()]
for i in xrange(k%n):
    x=ar.pop(n-1)
    ar.insert(0,x)
for i in xrange(q):
    print ar[int(sys.stdin.readline())]
