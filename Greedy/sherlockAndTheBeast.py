import sys
testcase=int(sys.stdin.readline())
adict={}
alist=[]
num=0
maxi=0
n33=0
n35=0
n53=0
n55=0
for x in xrange(3,100000+1):
    #print "in x loop"
    #print x
    if x==3:
        adict[3]=[1,0]
        #alist.append(3)
        continue
    if x==5:
        adict[5]=[0,1]
        #alist.append(5)
        continue
    #print alist
    #maxi=0
##    for i in alist:
##        for j in alist:
##            if i+j==x:
##                num=int(('555'*(adict[i][0]+adict[j][0]))+('33333'*(adict[i][1]+adict[j][1])))
##                if num>maxi:
##                    maxi=num
##                    adict[x]=[adict[i][0]+adict[j][0],adict[i][1]+adict[j][1]]
    
    if adict.has_key(x-3):
        n33=adict[x-3][0]+1
        n35=adict[x-3][1]
        adict[x]=[n33,n35]
    elif adict.has_key(x-5):
        n53=adict[x-5][0]
        n55=adict[x-5][1]+1
        adict[x]=[n53,n55]
    
        
    #if maxi!=0:
       #alist.append(x)
       #pass
    #print alist
#print "done"       
            
    
#print adict       
    
for t in xrange(testcase):
    n=int(sys.stdin.readline())
    if adict.has_key(n):
        print ('555'*adict[n][0])+('33333'*adict[n][1])
    else:
        print -1
