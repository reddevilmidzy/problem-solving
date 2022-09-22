from collections import deque
import sys
input = sys.stdin.readline

def topology(graph, w):
    queue = deque()
    ans = [0]*(n+1)
    for i in range(1, n+1):
        if dag[i]==0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        ans[node] += cost[node]
        for i in graph[node]:
            dag[i] -= 1
            ans[i] = max(ans[i], ans[node])
            if dag[i]==0:
                queue.append(i)
        
    return ans[w]


for _ in range(int(input())):
    n,k = map(int,input().split())
    cost = [0]+list(map(int,input().split()))
    dag = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        x,y = map(int,input().split())
        dag[y] += 1
        graph[x].append(y)
    w = int(input())
    print(topology(graph,w))
    # print(graph, dag)
