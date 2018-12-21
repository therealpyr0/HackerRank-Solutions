# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
s=sys.stdin.readline()
s=s.lower()
alist=[]
flag=1
for i in xrange(0,26):
    alist.append(0)
    
for i in s:
    if i==" ":
        continue
    alist[ord(i)-ord('a')]=1
for i in alist:
    if i!=1:
        flag=0
        break
        pass
if flag:
    print "pangram"
    pass
else :
    print "not pangram"