import sys
n=int(sys.stdin.readline())
ar=[int(i) for i in sys.stdin.readline().split()]
for i in xrange(1,n):
    j=i
    while ar[j]<ar[j-1] and j>=1:
        temp=ar[j-1]
        ar[j-1]=ar[j]
        ar[j]=temp
        j=j-1
    for j in xrange(n):
        print ar[j],
    print ""