from collections import deque
from sys import stdin
input = stdin.readline

def bfs(s):
    queue = deque()
    queue.append(s)
    visited = [False]*(n)
    visited[s] = True
    
    while queue:
        cur = queue.popleft()

        nxt = nums[cur]
        if cur + nxt < n and not visited[cur+nxt]:
            queue.append(cur+nxt)
            visited[cur+nxt] = True
        if 0 <= cur - nxt and not visited[cur-nxt]:
            queue.append(cur-nxt)
            visited[cur-nxt] = True
    
    return sum(visited)
n = int(input())
nums = list(map(int,input().split()))
s = int(input())
print(bfs(s-1))