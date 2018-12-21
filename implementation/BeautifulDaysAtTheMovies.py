# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
l=[int(i) for i in sys.stdin.readline().split(" ")]
c=0
for i in xrange(l[0],l[1]+1):
    if abs(i-int(str(i)[::-1]))%l[2]==0:
        c+=1
print c