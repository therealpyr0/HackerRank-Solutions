# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
h=int(sys.stdin.readline())
hashs="#"
for i in xrange(h):
    print hashs.rjust(h," ")
    hashs+="#"