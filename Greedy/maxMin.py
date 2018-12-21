import sys
n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
candies=[]
diff=0
mindiff=1000000000000
for i in xrange(n):
    candies.append(int(sys.stdin.readline()))
candies.sort()
#print candies
for i in xrange(0,n-k+1):
    a0=candies[i]
    a1=candies[i+k-1]
    #print "a0 : ",a0," a1 : ",a1
    diff=a1-a0
    if diff<mindiff:
        mindiff=diff
print mindiff
    
    

