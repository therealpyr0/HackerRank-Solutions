import sys
string = sys.stdin.readline().replace("\n","")
odd=0
alist=[]
for i in xrange(ord('a'),ord('z')+1):
    alist.append(0)
for i in xrange(len(string)):
    alist[ord(string[i])-ord('a')]=alist[ord(string[i])-ord('a')]+1
for i in alist:
    if i%2!=0:
        odd=odd+1
if odd>1:
    print "NO"
else:
    print "YES"
 
