from collections import deque

n = int(input())

a, b, x, y = map(int, input().split())

graph = [[-1]*n for _ in range(n)]

dx = [-2,-2,0,0,2,2]

dy = [-1,1,-2,2,-1,1]

def solution (a, b) :

    q = deque()

    q.append([a,b])

    graph[b][a] = 0

    while q:

        here = q.popleft();

        for i in range(6) :

            nx = here[0] + dx[i]

            ny = here[1] + dy[i]

            if (nx >= 0 and ny >= 0 and nx < n and ny < n) and graph[ny][nx] == -1 :

                q.append([nx, ny])

                graph[ny][nx] = graph[here[1]][here[0]] + 1

solution(a,b)

print(graph[y][x])