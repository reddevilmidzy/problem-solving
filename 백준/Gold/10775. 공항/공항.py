import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

g = int(input())
p = int(input())
parent = [i for i in range(g+1)]
ans = 0
for i in range(p):
    gi = int(input())
    gi_parent = find(parent, gi)
    if gi_parent == 0:
        break
    parent[gi_parent] = gi_parent-1
    ans += 1
print(ans)