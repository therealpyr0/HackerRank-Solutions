# Enter your code here. Read input from STDIN. Print output to STDOUT\
import sys
T=int(input())
for t in xrange(T):
    N=int(input())
    arr=[]
    arr=[int(i) for i in sys.stdin.readline().split()]
    if N%2==0:
        print "0"
        continue
    out=arr[0]
    for i in xrange(2,N,2):
        out=out^arr[i]
 
    print out
        
        