from collections import deque

def bfs():
    queue = deque()
    queue.append((n, 0))
    visited[n] = True
    while queue:
        c, cnt = queue.popleft()
        if c == k:
            print(cnt)
            break
        else:
            arr = [c-1, c+1, 2*c]
            for i in arr:
                if 0 <= i <= 100000:
                    if not visited[i]:
                        visited[i] = True
                        queue.append((i, cnt+1))
n, k = map(int, input().split())
visited = [False for i in range(100001)]
if n == k:
    print(0)
elif n > k:
    print(n-k)
else:
    bfs()