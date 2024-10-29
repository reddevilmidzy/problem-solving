import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().split())
nums = [sorted(list(map(int,input().split()))) for _ in range(n)]

res = int(1e9)
pos = [0]*n

max_val = max([nums[i][0] for i in range(n)])
hq = [[nums[i][0], i] for i in range(n)]
heapq.heapify(hq)

while hq:
    val,idx = heapq.heappop(hq)
    if res > max_val - val:
        res = max_val - val
    if pos[idx] == m:
        break
    heapq.heappush(hq, [nums[idx][pos[idx]], idx])
    max_val = max(max_val, nums[idx][pos[idx]])
    pos[idx] += 1
print(res)