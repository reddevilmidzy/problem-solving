import heapq, sys, math
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))

hq = []
high = max(nums)
for num in nums:
    heapq.heappush(hq, (2**int(math.log2(high//num)))*num)
ans = sys.maxsize

for _ in range(n*2):
    low = heapq.heappop(hq)
    if ans > high-low:
        ans = high-low
    heapq.heappush(hq, low*2)
    if low*2 > high:
        high = low*2
print(ans)