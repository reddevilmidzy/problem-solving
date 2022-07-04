import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append([pos[0][0], pos[0][1]])
    visited[0] = True
    while queue:
        x,y = queue.popleft()
        for i in range(len(pos)):
            if not visited[i]:
                mx,my = pos[i][0], pos[i][1]
                if abs(x-mx)+abs(y-my) <= 1000:
                    visited[i] = True
                    queue.append([mx,my])
                    if i == n+1:
                        return True
    return visited[-1]

t = int(input())
for _ in range(t):
    n = int(input())
    visited = [False for _ in range(n+2)]
    # 0:시작, 마지막: 페스티발
    pos = [list(map(int,input().rstrip().split())) for _ in range(n+2)]
    if bfs():
        print('happy')
    else:
        print('sad')