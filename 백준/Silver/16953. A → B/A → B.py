from collections import deque
a,b=map(int,input().split())
visited=dict()

def bfs():
    queue = deque()
    queue.append([a,1])
    visited[a] = 1
    while queue:
        q,cnt=queue.popleft()
        for move in [2*q, q*10+1]:
            if move <= b and move not in visited:
                if move ==b:
                    return cnt+1
                elif move > b//2:
                    continue
                else:
                    visited[move] = 1
                    queue.append([move,cnt+1])           
    return -1

print(bfs())