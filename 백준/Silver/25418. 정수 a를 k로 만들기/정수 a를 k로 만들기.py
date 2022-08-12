from collections import deque

def bfs():
    q = deque()
    q.append(a)
    visited = [-1]*(k+1)
    visited[a] = 0
    while q:
        move = q.popleft()
        for i in [move+1, move*2]:
            if i <= k and visited[i] == -1:
                visited[i] = visited[move]+1
                q.append(i)
    return visited[k]
a,k = map(int,input().split())

print(bfs())