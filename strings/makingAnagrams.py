# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
adict1={}
adict2={}
d=0
str1=sys.stdin.readline()
str2=sys.stdin.readline()   
(l1,l2)=len(str2),len(str2)
for i in xrange(ord('a'),ord('z')+1):
    d=d+abs(str1.count(chr(i))-str2.count(chr(i)))
    
print d
