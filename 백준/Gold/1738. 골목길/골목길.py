# from collections import deque
# import sys
# input = sys.stdin.readline
# INF = -int(1e9)

# def bellman(start, end):
#     dist = [INF for _ in range(n+1)]
#     ans = [n]
#     dist[start] = 0
#     go = [0]*(n+1)
#     for i in range(n-1):
#         for u,v,w in graph:
#             if dist[u] != INF and dist[u] + w > dist[v]:

#                 #if dist[u]+w>dist[v]:
            
#                 go[v] = u
#                 dist[v] = dist[u] + w
#                 #print('u',u,'v',v)
#                 #if route[u]==[]:

#                 # route[u].pop()
#                 # route[u] = [v]
    
#     for u,v,w in graph:
#         if dist[u] != INF and dist[u] + w > dist[v]:
#             if bfs(u,end):
#                 return [-1]
#     #print(go)
#     tmp = n
    
#     for i in range(n):
#         if tmp==1:
#             break
#         ans.append(go[tmp])
#         tmp = go[tmp]
#     #print(ans)
#     return reversed(ans)

# def bfs(start, end):
#     visit = [False]*(n+1)
#     visit[start] = True
#     queue = deque()
#     queue.append(start)
#     while queue:
#         node = queue.popleft()
#         if node==end:
#             return True
#         for i in route[node]:
#             if not visit[i]:
#                 visit[i] = True
#                 queue.append(i)
#     return False

# n,m = map(int,input().split())
# graph = []
# # route = [[INF]*(n+1) for _ in range(n+1)]
# route = [[] for _ in range(n+1)]
# for _ in range(m):
#     u,v,w = map(int,input().split())
#     # route[u][v] = w
#     graph.append([u,v,w])
#     route[u].append(v)
# print(*bellman(1, n))
# #print()

'''
벨만포드 사용하여 1부터 n까지의 최장거리 파악
-1을 출력해야하는 경우는 n까지 가는 도중 사이클 발생
사이클 발생은 벨만포드 사용으로 파악, n까지 도달 여부는 BFS 사용
방문 경로는 역추적 사용
'''


from collections import deque
import sys
input = sys.stdin.readline
# 최단경로 파악이 아니라 최장경로 파악이니 음의 무한
INF = -int(1e9)


# 역추적 ( 사실 DFS로 구현했었는데 너무 거추장스러움
def path(go):
	ans = [n]
	tmp = n

	for i in range(n):
		if tmp==1:
			break
		ans.append(go[tmp])
		tmp = go[tmp]
	return reversed(ans)

# 벨만포드 정의
def bellman(start, end):
    dist = [INF for _ in range(n+1)]
    ans = [n]
    dist[start] = 0
    go = [0]*(n+1)
    for i in range(n-1):
        for u,v,w in graph:
            if dist[u] != INF and dist[u] + w > dist[v]:            
                go[v] = u
                dist[v] = dist[u] + w

    # 음의 사이클 판별            
    for u,v,w in graph:
        if dist[u] != INF and dist[u] + w > dist[v]:
            if bfs(u,end): # n으로 가는 경로라면 -1
                return [-1]
    
    res = path(go)
    return res


# 사이클이 발생한 구간에서 n까지 갈 수 있는지 파악
# 만약 n까지 갈 수 있다면 return True
def bfs(start, end):
    visit = [False]*(n+1)
    visit[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node==end:
            return True
        for i in route[node]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)
    return False

n,m = map(int,input().split())
graph = []
route = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
	# 벨만포드용 그래프
    graph.append([u,v,w])
    # BFS용 그래프
    route[u].append(v)

print(*bellman(1, n))