import sys
N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))
changes=0
s=sum(B)
if s%2==0:
    s=0
    for i in range(N):
        s+=B[i]
        if s%2==0:
            pass
        else:
            changes+=2
    print changes
else:
    print"NO"