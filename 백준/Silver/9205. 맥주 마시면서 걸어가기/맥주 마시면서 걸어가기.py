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
    
    return visited[-1]

t = int(input())
for _ in range(t):
    n = int(input())
    pos = []
    visited = [False for _ in range(n+2)]
    pos.append(list(map(int,input().rstrip().split()))) # 첫번째 배열 시작 위치
    for i in range(n):
        pos.append(list(map(int,input().rstrip().split())))
    
    pos.append(list(map(int,input().rstrip().split()))) # 페스티발 마지막 배열
    
    # print('pos',pos)
    if bfs():
        print('happy')
    else:
        print('sad')