# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
testcase=int(sys.stdin.readline())
for t in xrange(testcase):
    sumleft=[0,]
    sumright=[0,]
    s=0
    found=0
    n=int(sys.stdin.readline())
    alist=[int(i) for i in sys.stdin.readline().split()]
    s=sum(alist)
    for i in xrange(0,n):
        x=sumleft[i]+alist[i]
        y=s-x+alist[i]
        if x==y:
            print "YES"
            found=1
            break
        sumleft.append(x)
        sumright.append(y)
    if found==0:
        print "NO"
    #print sumleft
    #print sumright
