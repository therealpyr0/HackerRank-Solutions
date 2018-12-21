import sys
n=int(sys.stdin.readline())
ar=[int(i) for i in sys.stdin.readline().split()]
for i in xrange(101):
    if ar.count(i)==1:
        print i
        break