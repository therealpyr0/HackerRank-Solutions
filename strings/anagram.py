# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
testcase=int(sys.stdin.readline())
for t in xrange(testcase):
    adict1={}
    adict2={}
    string=[]
    str1=[]
    l=0
    str2=[]
    changes=0
    string=list(sys.stdin.readline().replace("\n",""))
    l=len(string)
    if l%2!=0:
        print "-1"
        pass
    else:
        str1=string[0:l/2]
        str2=string[l/2:]
        for i in xrange(ord('a'),ord('z')+1):
            adict1[i]=str1.count(chr(i))
            adict2[i]=str2.count(chr(i))
        for i in xrange(ord('a'),ord('z')+1):
            changes=changes+abs(adict1[i]-adict2[i])
        print changes/2    
            
            
    