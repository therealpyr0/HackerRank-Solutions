# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
v=int(sys.stdin.readline())
n=int(sys.stdin.readline())
alist=[]
ar=sys.stdin.readline().split()
for i in xrange(len(ar)):
    if int(ar[i])==v:
        print i
        break
