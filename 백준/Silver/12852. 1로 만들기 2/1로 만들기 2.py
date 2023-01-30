from collections import deque
n = int(input())

def bfs():
    queue = deque()
    queue.append([1,0,[1]]) # now, cnt
    visited = [False] * (n+1)
    while queue:
        x,cnt,way = queue.popleft()
        if x == n:
            print(cnt)
            print(*reversed(way), sep=' ')
            return
        
        if x+1 <= n and not visited[x+1]:
            queue.append([x+1, cnt+1,way+[x+1]])
            visited[x+1] = True
            
        if x*3 <= n and not visited[x*3]:
            queue.append([x*3, cnt+1, way+[x*3]])
            visited[x*3] = True
        if x*2 <= n and not visited[x*2]:
            queue.append([x*2, cnt+1, way+[x*2]])
            visited[x*2] = True
bfs()