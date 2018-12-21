import sys
n=int(sys.stdin.readline())
templist=[]
mainlist=[]
anslist=[]
amap=[]
c=0
s=""
for x in xrange(n):
    amap.append(list(sys.stdin.readline()))
    
if n<=2:
    for i in xrange(len(amap)):
        for j in xrange(len(amap)):
            s=s+amap[i][j]
        print s
        s=""
    
else:
    
    anslist=amap
    for i in xrange(1,n-1):
        for j in xrange(1,n-1):
            #if max(amap[i][j],amap[i-1][j],amap[i][j-1],amap[i+1][j],amap[i][j+1])==amap[i][j]:
            templist.append(amap[i][j])
            templist.append(amap[i-1][j])
            templist.append(amap[i][j-1])
            templist.append(amap[i+1][j])
            templist.append(amap[i][j+1])
            m=max(templist)
            c=templist.count(m)
            templist=[]
            if m==amap[i][j]:
                if c==1:
                    anslist[i][j]='X'
                
                #anslist[i][j]='X'
    for i in xrange(len(anslist)):
        for j in xrange(len(anslist)):
            s=s+anslist[i][j]
        print s
        s=""
