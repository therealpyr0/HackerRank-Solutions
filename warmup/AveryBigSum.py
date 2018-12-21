# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
x=sys.stdin.readline()
alist=[int(i) for i in sys.stdin.readline().split()]
print sum(alist)