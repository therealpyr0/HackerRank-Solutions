# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
a=pow(2,32)
testcase=int(sys.stdin.readline())
for i in xrange(testcase):
    n=int(sys.stdin.readline())
    print str(a-n-1).replace("L","")