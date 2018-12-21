# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math
testcase=int(sys.stdin.readline())
for t in xrange(testcase):
    count=0
    (a,b)=[int(i) for i in sys.stdin.readline().split()]
    up=int(math.sqrt(b)+2)
    for i in xrange(1,up):
           x=i**2
           if x>=a and x<=b:
                count=count+1
    print count
           