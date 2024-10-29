import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().split())
nums = [sorted(list(map(int,input().split()))) for _ in range(n)]

res = int(1e9)
pos = [0]*n

max_val = 0
hq = []

for i in range(n):
    heapq.heappush(hq, (nums[i][0], i))
    max_val = max(max_val, nums[i][0])

while hq:
    val,idx = heapq.heappop(hq)
    if res > max_val - val:
        res = max_val - val
    if pos[idx] + 1 == m:
        break
    pos[idx] += 1
    heapq.heappush(hq, (nums[idx][pos[idx]], idx))
    max_val = max(max_val, nums[idx][pos[idx]])
print(res)