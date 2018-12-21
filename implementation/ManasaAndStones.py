# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
testcase=int(sys.stdin.readline())
for t in xrange(testcase):
    #alist=[]
    #temp=[]
    #ans=[]
    #alist.append(0)
    x=0
    m=0
    n=int(sys.stdin.readline())
    a=int(sys.stdin.readline())
    b=int(sys.stdin.readline())
    if b>a:
        x=a*(n-1)
        m=b*(n-1)
    else:
        x=b*(n-1)
        m=a*(n-1)
    diff=b-a
    while x<=m:
        print x,
        x=x+abs(b-a)
        if diff==0:
            break
    #for i in ans:
    #    print i,
    print ""    
    
