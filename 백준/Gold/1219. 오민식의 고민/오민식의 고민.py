from collections import deque
import sys
input = sys.stdin.readline
INF = -int(1e9) # 음의 ㅜ한
def bellman(start,end):
    dist = [INF for _ in range(n)] # 초기배열
    dist[start] = money[start] # 가만히 있는경우를 위해 0이 아닌 money[start]로 초기화
    
    for i in range(n-1):
        for u,v,w in city: # 한바퀴 돌아서 갱신
            if dist[u] != INF and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
    
    if dist[end] == INF: # 도착불가능 gg
        return 'gg'
    
    # print(city, dist)
	# 한번 더 돌았을 때 사이클이 생긴다면
    for u,v,w in city:
        # print(dist[u], w, dist[v])
        if dist[u] != INF and dist[u] + w > dist[v]:
            if bfs(v,end): # 사이클이 생겼고, 그 사이클에서 도착가능하다면
                return 'Gee'
            else:
                pass

    # 최대머니 리턴        
    return dist[end]


def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [False]*(n)
    visited[start] = True
    while q:
        now = q.popleft()
        if now == end:
            return True
        for a,b,c in city:
            if a==now:
                if not visited[b]:
                    visited[b] = True
                    q.append(b)
    
    return False



n,start,end,m = map(int,input().split()) # 노드개수, 시작, 끝, 간선개수
city = []
for _ in range(m):
    a,b,c = map(int,input().split()) # 시작, 끝, 교통비
    city.append([a,b,-c]) # 교통비는 음수로
money = list(map(int,input().split())) # 방문시 얻는 돈 입력받음
for i in range(m):
    city[i][2] = city[i][2]+money[city[i][1]] # 교통비+방문시 얻는 돈
# print(city)
print(bellman(start,end))

# 반례 
"""4 0 3 4
0 1 0
1 2 0
2 1 0
0 3 10
10 10 10 10"""