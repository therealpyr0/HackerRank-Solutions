# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N=int(sys.stdin.readline())
col1=0
sum1=0
sum2=0
col2=N-1
for i in xrange(N):
    nos=[]
    nos=[int(i) for i in sys.stdin.readline().split()]
    sum1+=nos[col1]
    col1+=1
    sum2+=nos[col2]
    col2-=1
print abs(sum1-sum2)
    