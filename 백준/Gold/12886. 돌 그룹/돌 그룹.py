from collections import deque
import sys
input = sys.stdin.readline

def nxt(x: int, y: int) -> tuple[int]:
    min_v = min(x, y)
    max_v = max(x, y)

    return (min_v + min_v, max_v - min_v)

nums = tuple(sorted(list(map(int,input().split()))))

def bfs(a:int, b:int, c:int):
    queue = deque()
    queue.append((a,b,c))
    visited = set()
    visited.add((a,b,c))

    while queue:
        cur = queue.popleft()
        if cur[0] == cur[2]:
            return 1
        for i,j,k in ((0,1,2), (1,2,0), (0,2,1)):
            if cur[i] == cur[j]: continue
            y,x = nxt(cur[i], cur[j])
            tmp = tuple(sorted((y,x,cur[k])))
            if tmp not in visited:
                visited.add(tmp)
                queue.append(tmp)
    return 0

print(bfs(*nums))