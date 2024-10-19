from heapq import heappush,heapreplace
import sys
input = sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
nums.sort()

hq = []

for i in range(n):
    if hq and hq[0] <= nums[i]:
        heapreplace(hq, hq[0] + 1)
    else:
        heappush(hq, 1)

print(len(hq))