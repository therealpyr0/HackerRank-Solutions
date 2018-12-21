# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math
ans=0
testcase=int(sys.stdin.readline())
def isprime(x):
    if x==1:
        return 0
    for a in xrange(2,int(math.sqrt(x))+1):
        if x%a==0:
            return 0
    return 1
wayslist=[]
anslist=[]
counter=0
ways=0
temp=1
upper=0
def calculateways(a,b):
    temp=1
    if a>=b:
        upper=a
        lower=b
        
    else:
        upper=b
        lower=a
    #print "in func"
    #print upper
    #print lower
    for c in xrange(a+b,upper,-1):
        #print "in loop"
        temp=temp*c
    ans=temp/math.factorial(lower)
    return ans

for t in xrange(testcase):
    n=int(sys.stdin.readline())
    x=n/4
    #print x
    for i in xrange(x+1):
        #print str(n-(4*i))+" "+str(i)
        ways=ways+calculateways(n-(4*i),i)
    wayslist.append(ways)
    ways=0
for i in wayslist:
    #print "no : "+str(i)
    for j in xrange(2,int((i)+1)):
        if isprime(j)==1:
            #print "prime : "+str(j)
            counter=counter+1
    print counter
    counter=0
