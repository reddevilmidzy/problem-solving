from collections import deque

def bfs():
    queue = deque([n])
    visited[n][0] = 0 # 방문 처리
    visited[n][1] = 1 # 방법
    while queue:
        q= queue.popleft()
        arr = [q-1, q+1, q*2]
        for i in arr:
            if -1 < i < 100001:
                if visited[i][0] == -1: # 방문한적 없다면
                    visited[i][0] = visited[q][0] + 1 # 방문한다.
                    visited[i][1] = visited[q][1] # 횟수
                    queue.append(i)
                elif visited[i][0] == visited[q][0] + 1:
                    visited[i][1] += visited[q][1]



n, k = map(int, input().split())
visited = [[-1,0] for i in range(100001)] # 첫번째 값은 도달 초, 두번째 값은 방법
if n == k:
    print(0)
    print(1)
elif n > k:
    print(n-k)
    print(1)
else:
    # visited[n][0] = 0
    # visited[n][1] = 1
    bfs()
    print(visited[k][0], visited[k][1], sep='\n')
    #print(bfs())