# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
testcase=int(sys.stdin.readline())
for t in xrange(testcase):
    m=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    table=[]
    cost=[int(i) for i in sys.stdin.readline().split()]
    for i in xrange(n):
        x=m-cost[i]
        if x in cost[0:i]:
            j=cost[0:i].index(m-cost[i])    
            break
        if x in cost[i+1:]:
            j=cost[i+1:].index(m-cost[i])
    if i>j:
        i,j=j,i
    print i+1,j+1
