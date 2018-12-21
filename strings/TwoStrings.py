# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
T=int(sys.stdin.readline().replace("\n",""))
for t in xrange(T):
    s1=sys.stdin.readline().replace("\n","")
    s2=sys.stdin.readline().replace("\n","")
    adict={}
    flag=0
    bdict={}
    for i in xrange(ord('a'),ord('z')+1):
        #adict[chr(i)]=0
        #bdict[chr(i)]=0
        x=chr(i)
        #a=x in s1
        #print i," ",x
        #b=x in s2
        if (x in s1) and (x in s2):
            print "YES"
            flag=1
            break
        else:
            continue
    if flag==0:
        print "NO"
    
    