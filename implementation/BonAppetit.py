# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n,k=sys.stdin.readline().split(" ")
n=int(n)
k=int(k)
all=[int(i) for i in sys.stdin.readline().split(" ")]
charged=int(sys.stdin.readline())
actual=(sum(all)-all[k])/2
x=charged-actual
if x==0:
    print "Bon Appetit"
else:
    print x