from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n,s,p = map(int,input().split())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    return bfs(p, tree, n, s)

def bfs(st:int, tree: list[list[int]], n: int, s: int):
    queue = deque()
    queue.append((st, 0))
    visited = [False]*(n+1)
    visited[st] = True
    res = 0
    twice = False
    while queue:
        node, cnt = queue.popleft()

        if node <= s: # 지지대 얼음판에 도착
            res += cnt
            if not twice: # 첫번째라면
                twice = True
            else:
                return n - res - 1
        for nxt in tree[node]:
            if not visited[nxt]:
                queue.append((nxt, cnt+1))
                visited[nxt] = True

print(solve())