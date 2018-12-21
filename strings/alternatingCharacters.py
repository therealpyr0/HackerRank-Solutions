# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
anslist=[]
testcase=int(sys.stdin.readline())
slist=[]
counter=0
for i in xrange(testcase):
    slist.append(sys.stdin.readline())
    pass
for s in slist:
    while s.count("AA")+s.count("BB")>=1:
        if "AA" in s:
            counter=counter+s.count("AA")
            
            s=s.replace("AA","A")
        
        if "BB" in s:
            counter=counter+s.count("BB")
            s=s.replace("BB","B")
           
        
    anslist.append(counter)
    counter=0
            #print s
            
            
    
for i in anslist:
    print i
    