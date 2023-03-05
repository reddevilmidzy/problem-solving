import heapq

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    hq = []
    
    for u,v,w in costs:
        heapq.heappush(hq, [w, u, v])
    
    parent = [i for i in range(n+1)]
    edges = n-1
    while hq:
        c,a,b = heapq.heappop(hq)
        
        if find(parent, a) != find(parent, b):
            answer += c
            union(parent, a, b)
            edges -= 1
        
        if not edges:
            break
    
    return answer