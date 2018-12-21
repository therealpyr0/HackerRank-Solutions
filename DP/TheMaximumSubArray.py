import sys
testcase=int(sys.stdin.readline())
for t in xrange(testcase):
    non=0
    cont=0
    m1=0
    m2=0
    n=int(sys.stdin.readline())
    nos=[int(i) for i in sys.stdin.readline().split()]
    for i in xrange(n):
        m1=m1+nos[i]
        if m1<0:
            m1=0
            pass
        if m2<m1:
            m2=m1
        if nos[i]>0:
            non=non+nos[i]
    if non==0:
        non=max(nos)
        m2=non
    print m2,non
