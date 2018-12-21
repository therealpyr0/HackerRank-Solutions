import sys
T=int(sys.stdin.readline())
for t in xrange(T):
    n,k=[int(i) for i in sys.stdin.readline().split()]
    time=[int(i) for i in sys.stdin.readline().split()]
    stu=0
    for i in time:
        if i<=0:
            stu=stu+1
    if stu<k:
        print "YES"
    else:
        print "NO"
