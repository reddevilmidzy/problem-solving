from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)

def solve(n:int, nums:list[int]):
    pre = set()
    st = dict()
    ed = dict()
    val = [INF]

    for i in range(n):
        st[nums[n-i-1]] = n-i-1
        ed[nums[i]] = i

    for idx,num in enumerate(nums):
        if num > val[0]:
            return "No"
        if st[num] == ed[num]: continue
        elif st[num] == idx:
            heappush(val, num)
            pre.add(num)
        elif ed[num] == idx:
            pre.remove(num)
            if val[0] == num:
                heappop(val)
    return "Yes"

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    print(solve(n,nums))