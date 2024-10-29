from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n,a,b = map(int,input().split())
hq = []
for _ in range(n):
    u,v = map(int,input().split())
    heappush(hq, (u-v, u, v))
res = 0
for _ in range(a):
    res += heappop(hq)[1]
for _ in range(b):
    res += heappop(hq)[2]
print(res)