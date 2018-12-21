# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
T=int(sys.stdin.readline())
for t in xrange(T):
    N=int(sys.stdin.readline())
    mat=[]
    temp=[]
    check=True
    for n in xrange(N):
        temp=list(sys.stdin.readline().strip())
        temp.sort()
        mat.append(temp)
    for i in xrange(N-1):
        for j in xrange(N):
            if ord(mat[i][j])<=ord(mat[i+1][j]):
                pass
            else:
                check=False
                break
    #print mat
    if check:
        print "YES"
    else:
        print "NO"
        