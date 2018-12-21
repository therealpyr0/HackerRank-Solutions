# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
gemlist=[]
gems=[]
counter=0
found=1
n=int(sys.stdin.readline())
for i in xrange(n):
    gemlist.append(sys.stdin.readline().replace("\n",""))
for i in xrange(ord('a'),ord('z')+1):
    found=1
    for j in xrange(n):
        if chr(i) in gemlist[j]:
            continue
        else:
            found=0
            break
    if found==1:
        counter=counter+1
            
print counter
