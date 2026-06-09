import sys
tree=[0]*1010
n=0
for line in sys.stdin.readlines():
    t=list(line.split())
    t[0]=int(t[0])
    n=max(n,t[0])
    tree[t[0]]=t[1]
def in_traverse(x):
    i=x
    if tree[2*i+1]!=0:
        in_traverse(2*i+1)
    print(tree[i][0],end=' ')
    if tree[2*i+2]!=0:
        in_traverse(2*i+2)
in_traverse(0)
    