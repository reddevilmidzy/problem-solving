from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]
nums.sort(key=lambda x: (x[-1], -x[0]))

hq = []
for p, d in nums: 
    if len(hq) < d:
        heappush(hq, (p, -d))
    else:
        if hq and hq[0][0] <= p and len(hq) >= d:
            heappop(hq)
        if len(hq) < d:
            heappush(hq, (p, -d))
res = 0
while hq:
    p,d = heappop(hq)
    res += p
print(res)