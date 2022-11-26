import sys
input = sys.stdin.readline

def find(parent, x):
    while x != parent[x]:
        x = parent[x]
    return x

g = int(input())
p = int(input())
parent = [i for i in range(g+1)]
ans = 0
for i in range(p):
    gi = int(input())
    gi_parent = find(parent, gi)
    parent[gi] = gi_parent
    
    if gi_parent == 0:
        break
    parent[gi_parent] = gi_parent-1
    ans += 1
print(ans)