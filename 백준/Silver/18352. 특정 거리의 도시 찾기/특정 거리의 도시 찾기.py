import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int, input().rstrip().split())
city = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().rstrip().split())
    city[a].append(b)

answer = []
def bfs():
    queue = deque()
    queue.append((x,0))
    visited[x] = True
    while queue:
        t, c = queue.popleft()
        if c == k:
            answer.append(t)
        elif c < k:
            for i in city[t]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, c+1))

bfs()
print(-1) if len(answer)==0 else print(*sorted(answer), sep='\n')