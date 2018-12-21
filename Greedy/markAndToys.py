# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
(n,k)=[int(i) for i in sys.stdin.readline().split()]
price=[int(i) for i in sys.stdin.readline().split()]
spent=0
toys=0
while 1:
    x=price.pop(price.index(min(price)))
    if spent+x<=k:
        spent=spent+x
        toys=toys+1
        pass
    else:
        break
print toys

    
    
