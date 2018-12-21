# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
T=int(sys.stdin.readline())
for t in xrange(T):
    b,w=[int(i) for i in sys.stdin.readline().split()]
    x,y,z=[int(i) for i in sys.stdin.readline().split()]
    total=0
    if (x+z)<y:
        total=(b*x)+((x+z)*w)
    elif (y+z)<x:
        total=((y+z)*b)+(w*y)
    else:
        total=(b*x)+(y*w)
    print total
        
        