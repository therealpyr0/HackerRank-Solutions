import sys
n=int(sys.stdin.readline())
ar=[int(i) for i in sys.stdin.readline().split()]
#for j in xrange(0,n):
#    if ar[j]<=x:
#        i=i+1
#        ar[i],ar[j]=ar[j],ar[i]
#ar[i+1],ar[n-1]=ar[n-1],ar[i+1]
#print ar
l1=[]
l2=[]
l3=[]
l3.append(ar[0])
for i in xrange(1,n):
    if ar[i]>ar[0]:
        l2.append(ar[i])
    if ar[i]<ar[0]:
        l1.append(ar[i])
    if ar[i]==ar[0]:
        l3.append(ar[i])
for i in xrange(len(l1)):
    print l1[i],
for i in xrange(len(l3)):
    print l3[i],
for i in xrange(len(l2)):
    print l2[i],
