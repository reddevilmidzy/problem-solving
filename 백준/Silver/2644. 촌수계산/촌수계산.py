import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((to,0))
    visited[to] = True
    while queue:
        person,chon = queue.popleft()
        for i in fam[person]:
            if not visited[i]:
                if i == fromm:
                    return chon+1
                visited[i] = True
                queue.append((i,chon+1))
    return -1

n =int(input())
fam = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
to, fromm = map(int,input().rstrip().split())
for i in range(int(input())):
    x,y = map(int,input().rstrip().split())
    fam[x].append(y)
    fam[y].append(x)

print(bfs())