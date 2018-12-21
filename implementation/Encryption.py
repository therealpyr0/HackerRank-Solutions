# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math
templist=[]
mainlist=[]
counter=0
string=sys.stdin.readline().replace("\n","")
string.replace(" ","")
#print string
w=math.floor(math.sqrt(len(string)))
h=math.ceil(math.sqrt(len(string)))
w=int(w)
h=int(h)
#print w
#print h
if h*w>=len(string):
    pass
else:
    w=w+1
for i in xrange(len(string)):
    templist.append(string[i])
    if (i+1)%h==0:
        mainlist.append(templist)
        templist=[]
    if (i+1)==len(string):
        mainlist.append(templist)
        templist=[]
        break
#print mainlist
astr=""
for i in xrange(h):
    for j in xrange(w):
        try:
            astr=astr+mainlist[j][i]
        except:
            pass
    print astr,
    astr=""
