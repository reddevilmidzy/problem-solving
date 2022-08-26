from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = [[] for i in range(n)]

def bfs(s,e):
    queue = deque()
    queue.append([s, 0])
    visited = [False]*(n)
    visited[s] = True
    while queue:
        q, cnt = queue.popleft()
        if q == e:
            return cnt
        for i in tree[q]:
            if not visited[i[0]]:
                queue.append([i[0], cnt+i[1]])
                visited[i[0]] = True

for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a-1].append((b-1,c))
    tree[b-1].append((a-1,c))

for _ in range(m):
    i,j = map(int,input().split())
    print(bfs(i-1,j-1))