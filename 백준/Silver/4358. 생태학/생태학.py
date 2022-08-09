from collections import defaultdict
import sys
input = sys.stdin.readline
tree=defaultdict(int)
sor = 0

while True:
    t=input().rstrip()
    if not t:
        break
    sor += 1
    tree[t]+=1
for k,v in sorted(tree.items()):
    print("%s %.4f" % (k,v/sor*100))