import sys
input = sys.stdin.readline

def solve(tree):
    leaf = [i for i in range(n) if len(tree[i]) == 1]
    visited = [0]*n
    while leaf:
        node = leaf.pop()
        for par in tree[node]:
            for gra_par in tree[par]:
                tree[gra_par].remove(par)
                if len(tree[gra_par]) == 1:
                    leaf.append(gra_par)
            visited[par] = 1
            tree[par].clear()
    return sum(visited)
        
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

print(solve(tree))