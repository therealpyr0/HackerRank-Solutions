# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
testcase=int(sys.stdin.readline())
anslist=[]
counter=0
digit=0
number=0
for i in xrange(testcase):
    number=int(sys.stdin.readline())
    num=number
    while number:
        digit=number%10
        if digit!=0:
            if num%digit==0:
                counter=counter+1
                pass
        number=number/10
    anslist.append(counter)
    counter=0
for i in anslist:
    print i