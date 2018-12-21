import sys
n=int(sys.stdin.readline())
alist=[int(i) for i in sys.stdin.readline().split()]
steps=0
l=0
tocut=0
topop=[]
while 1:
    if len(alist)==1 and alist[0]==0:
        break
    while 1:
        try:
            m=min(alist)
            if m>0:
                break
            else:
                alist.pop(alist.index(min(alist)))
        except:
            break
            pass
    l=len(alist)
    if l==0:
        break
    tocut=min(alist)
    if tocut==0:
        break
    for i in xrange(l):
        if alist[i]>=tocut:
            alist[i]=alist[i]-tocut
            steps=steps+1
    #print alist
    if steps==0:
        break
    else:
        print steps
        steps=0
