# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
(n,testcase)=[int(i) for i in sys.stdin.readline().split()]
w=[]
a1=0
a2=0
w=[int(i) for i in sys.stdin.readline().split()]
for t in xrange(testcase):
    (a1,a2)=[int(i) for i in sys.stdin.readline().split()]
    print min(w[a1:(a2+1)])
        
    
    