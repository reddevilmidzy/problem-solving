import sys
input=sys.stdin.readline
INF=int(1e9) # 무한

def bf(start):
    dist[start]=0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0] # 현재 노드
            next_node = edges[j][1] # 다음 노드
            cost = edges[j][2] # 이동 비용

            if dist[cur] != INF and dist[next_node] > dist[cur]+cost:
                dist[next_node] = dist[cur]+cost
                if i == n-1: # 한바퀴 돌았고 다시 한번 돌았는데 값이 갱신된다면 무한 사이클
                    return True

    return False

n,m = map(int,input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

negative_cycle = bf(1)
if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])