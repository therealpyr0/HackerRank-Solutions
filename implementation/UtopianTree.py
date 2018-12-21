# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
testcase=int(sys.stdin.readline())
anslist=[]
height=1
for i in xrange(testcase):
    n=int(sys.stdin.readline())
    for j in xrange(1,(n+1)):
        if j%2!=0:
            height=height*2
            pass
        if j%2==0:
            height=height+1
            pass
    anslist.append(height)
    height=1
for i in anslist:
    print i
    