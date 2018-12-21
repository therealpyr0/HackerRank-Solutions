# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
(v,e)=[int(i) for i in sys.stdin.readline().split()]
tree={}
leafnodes=[]
edges=[]
childrenlist={}
for i in xrange(e):
    e=[]
    (c,p)=[int(i) for i in sys.stdin.readline().split()]
    e.append(c)
    e.append(p)
    edges.append(e)
    if tree.has_key(p):
        tree[p].append(c)
        pass
    else:
        temp=[]
        temp.append(c)
        tree[p]=temp
#print edges
#print tree
for i in tree:
    stack=[]
    c=len(tree[i])
    for j in tree[i]:
        stack.append(j)
    for j in stack:
        if tree.has_key(j):
            c=c+len(tree[j])
            for l in tree[j]:
                stack.append(l)
    childrenlist[i]=c
    c=0
#print childrenlist
cut=0
for e in edges:
    c=e[0]
    p=e[1]
    try:
        c1=childrenlist[c]+1
    except:
        c1=0
    p1=v-c1
    if c1%2==0 and p1%2==0 and c1!=0:
        cut=cut+1
        #print "in cut",e
        childrenlist[p]=childrenlist[p]-c1
print cut

    
