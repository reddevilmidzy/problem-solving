import sys, heapq
input = sys.stdin.readline

def solution():
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))

    heapq.heapify(nums)

    for i in range(m):
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        heapq.heappush(nums, a+b)
        heapq.heappush(nums, a+b)
    return sum(nums)
print(solution())