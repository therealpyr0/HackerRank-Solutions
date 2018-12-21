# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
T=int(sys.stdin.readline().replace("\n",""))
for t in xrange(T):
    string=sys.stdin.readline().replace("\n","")
    l=len(string)
    r=l-1
    flag=0
    rev=string[::-1]
    for i in xrange(1,l):
        if abs(ord(string[i])-ord(string[i-1]))!=abs(ord(rev[i])-ord(rev[i-1])):
            print "Not Funny"
            flag=1
            break
            pass
    if flag==0:
        print "Funny"
        