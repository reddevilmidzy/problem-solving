import sys, heapq
input = sys.stdin.readline

INF = int(1e9) + 7
n,m = map(int,input().split())
nums = [sorted(list(map(int,input().split()))) for _ in range(n)]

res = []
pos = [0]*n

max_val = max([nums[i][0] for i in range(n)])
hq = [[nums[i][0], i] for i in range(n)]
heapq.heapify(hq)

while hq:
    val,idx = heapq.heappop(hq)
    res.append(max_val - val)
    if pos[idx] == m:
        break
    heapq.heappush(hq, [nums[idx][pos[idx]], idx])
    max_val = max(max_val, nums[idx][pos[idx]])
    pos[idx] += 1
print(min(res))