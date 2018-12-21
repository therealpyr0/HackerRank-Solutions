# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
testcase=int(sys.stdin.readline())
anslist=[]
s=""
l=0
count=0
for i in xrange(testcase):
    s=str(sys.stdin.readline())
    l=len(s)
    count=0
    if i!=testcase-1:
        l=l-1
    for j in xrange((l/2)):
        count=count+abs(ord(s[j])-ord(s[l-j-1]))
    anslist.append(count)
for i in anslist:
    print i