# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
testcase=int(sys.stdin.readline())
choco=0
ans=0
anslist=[]
w=0
new=0
counter=0
for x in xrange(testcase):
    (n,c,m)=sys.stdin.readline().split()
    n=int(n)
    m=int(m)
    c=int(c)
    choco=int(n/c)
    w=choco
    counter=0
    while w>=m:
        new=int(w/m)
        w=w%m
        w=w+new
        counter=counter+new
        #print "w : "+str(w)
    anslist.append(counter+choco)
for i in anslist:
    print i
        