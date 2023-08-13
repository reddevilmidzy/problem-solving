from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
m = int(input())
edges = [list(map(int,input().split())) for _ in range(m)]
visited = set()
hq = [(0, tuple(nums))]

while hq:
    dist, cur = heappop(hq)
    if cur in visited: continue
    visited.add(cur)

    # 모든 것이 True 면 True 반환
    if all(cur[i] <= cur[i+1] for i in range(n-1)):
        print(dist)
        break
    for u,v,w in edges:
        tmp = list(cur)
        tmp[u-1],tmp[v-1] = tmp[v-1], tmp[u-1]
        heappush(hq, (dist+w, tuple(tmp)))
else:
    print(-1)