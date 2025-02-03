import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().rstrip().split()))
cur = 0
ans = nums[0]

for i in nums:
    cur = max(i, cur+i)
    ans = max(ans, cur)
print(ans)