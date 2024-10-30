from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
hq = []
res = 0
# b가 더 큰경우도 있을 수 있음
for i in range(m):
    res += a[i]
    if a[i] == 100:
        pass
    elif a[i] + b[i] <= 100:
        heappush(hq, (-b[i], a[i]))
    else:
        heappush(hq, (-100 + a[i], a[i]))

n *= 24
while hq:
    u,v = heappop(hq)
    diff = 100 - v
    tmp = diff // (-u)
    if n - tmp >= 0:
        n -= tmp
        v += tmp * -u
        res += tmp * -u
        if v < 100:
            heappush(hq, (-100 + v, v))
    else:
        res += n * -u 
        break
    if n <= 0: break

print(res)
