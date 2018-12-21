# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
a,b,N=[int(i) for i in sys.stdin.readline().replace("\n","").split()]
for i in xrange(N-2):
    n=pow(b,2)+a
    a=b
    b=n
    #print i
print b