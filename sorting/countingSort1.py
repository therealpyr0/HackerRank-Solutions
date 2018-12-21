# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n=int(sys.stdin.readline())
ar=[int(i) for i in sys.stdin.readline().split()]
for i in xrange(100):
    print ar.count(i),
    