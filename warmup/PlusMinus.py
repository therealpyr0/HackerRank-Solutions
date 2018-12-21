# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N=int(sys.stdin.readline())
pos=0
neg=0
zero=0
nos=[int(i) for i in sys.stdin.readline().split()]
for i in xrange(N):
    if nos[i]==0:
        zero+=1
        continue
        pass
    if nos[i]<0:
        neg+=1
        continue
        pass
    if nos[i]>0:
        pos+=1
        continue
        pass
N=float(N)
print pos/N
print neg/N
print zero/N
    