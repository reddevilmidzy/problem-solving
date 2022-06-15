from collections import deque

def bfs(n):
    visited = [False] * 100001
    queue = deque()
    queue.append([n, 0])
    visited[n] = True
    while queue:
        now, cnt = queue.popleft()
        if now == k:
            return cnt
        for n in ([now-1,now*2,now+1]):
            if 0 <= n <= 100000:
                if not visited[n]:
                    visited[n] = True
                    if n == now*2:
                        queue.append([n,cnt])
                    else:
                        queue.append([n, cnt+1])

n,k = map(int,input().rstrip().split())
ans = 0


if n == k:
    pass
elif n > k:
    ans = n-k
else:
    ans = bfs(n)
print(ans)