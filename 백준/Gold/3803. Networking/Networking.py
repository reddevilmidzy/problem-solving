import sys, heapq
input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a,b):
    a = find(parent,a)
    b = find(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


def solve(h,n):
    ans = 0
    stop = n-1
    while h:
        w,u,v = heapq.heappop(h)
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            ans += w
            stop -= 1

        if stop==0:
            break
    return ans 


while True:
    tmp = list(map(int,input().split()))
    if tmp[0]==0:
        break
    n,m = tmp[0],tmp[1]
    h = []
    parent = [i for i in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        heapq.heappush(h, (w,u,v))

    res = solve(h, n)
    print(res)
    input()