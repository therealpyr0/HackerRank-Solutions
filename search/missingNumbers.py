# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n=int(sys.stdin.readline())
l=[int(i) for i in sys.stdin.readline().split()]
adict={}
ans=[]
for i in l:
    if adict.has_key(i):
        adict[i]=adict[i]+1
    else:
        adict[i]=1
        pass
m=int(sys.stdin.readline())
l=[]
l=[int(i) for i in sys.stdin.readline().split()]
bdict={}
for i in l:
    if bdict.has_key(i):
        bdict[i]=bdict[i]+1
    else:
        bdict[i]=1
        pass    
for i in bdict:
    if adict.has_key(i):
        if adict[i]-bdict[i]==0:
            pass
        else:
            ans.append(i)
    else:
        ans.append(i)
ans.sort()
for i in ans:
    print i,