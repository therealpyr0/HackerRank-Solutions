# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n=int(sys.stdin.readline())
ar=[int(i) for i in sys.stdin.readline().split()]
ar.sort()
print ar[n/2]