import math
from collections import defaultdict, deque

def bfs(st: int, ed: int):
    queue = deque()
    queue.append((st, 0))
    visited = defaultdict(bool)
    visited[st] = True

    while queue:
        cur, cnt = queue.popleft()
        if cur == ed:
            return cnt

        if cur - 1 > 0 and not visited[cur-1]:
            queue.append((cur-1, cnt+1))
            visited[cur-1] = True
        if not visited[cur+1]:
            queue.append((cur+1, cnt+1))
            visited[cur+1] = True
        for i in range(int(math.log2(cur))):
            if not visited[cur^(2**i)]:
                queue.append((cur^(2**i), cnt+1))
                visited[cur^(2**i)] = True

st = int(input(), 2)
ed = int(input(), 2)
print(bfs(st, ed))