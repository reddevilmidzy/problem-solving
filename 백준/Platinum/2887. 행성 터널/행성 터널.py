import sys, heapq
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
all_path = []
sort_x = []
sort_y = []
sort_z = []

parent = [i for i in range(n)]

for i in range(n):
    x,y,z = map(int,input().split())

    heapq.heappush(sort_x, [x,y,z,i])
    heapq.heappush(sort_y, [y,z,x,i])
    heapq.heappush(sort_z, [z,x,y,i])

pre_x = heapq.heappop(sort_x)
pre_y = heapq.heappop(sort_y)
pre_z = heapq.heappop(sort_z)

for _ in range(n-1):
    aft_x = heapq.heappop(sort_x)
    aft_y = heapq.heappop(sort_y)
    aft_z = heapq.heappop(sort_z)
    
    heapq.heappush(all_path, [abs(pre_x[0]-aft_x[0]),pre_x[-1], aft_x[-1]]) # 가는 비용, i->j
    heapq.heappush(all_path, [abs(pre_y[0]-aft_y[0]),pre_y[-1], aft_y[-1]])
    heapq.heappush(all_path, [abs(pre_z[0]-aft_z[0]),pre_z[-1], aft_z[-1]])
    pre_x = aft_x
    pre_y = aft_y
    pre_z = aft_z
    
ans = 0
edges = 0

while all_path:
    cost, a,b = heapq.heappop(all_path)
    if find_parent(parent,a) != find_parent(parent,b):
        ans += cost
        union_parent(parent,a,b)
        edges += 1
    
    if edges==n-1:
        break

print(ans)