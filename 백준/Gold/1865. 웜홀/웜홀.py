import sys
input = sys.stdin.readline

def bellman_ford(graph, start):
    distance= dict()
    for node in graph:
        distance[node] = 5000 * 10000
    distance[start] = 0

    for i in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]
    
    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return 'YES'
    
    return 'NO'


for _ in range(int(input())):
    n,m,w = map(int,input().split())
    graph = dict()
    for i in range(1, n+1):
        graph[i] = {}

    for j in range(m):
        s,e,t=map(int,input().split())
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], t)
        else:
            graph[s][e] = t

        if s in graph[e]:
            graph[e][s] = min(graph[e][s], t)
        else:
            graph[e][s] = t

    for k in range(w):
        s,e,t = map(int,input().split())
        graph[s][e] = -t

    print(bellman_ford(graph, 1))