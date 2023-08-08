n = int(input())
nums = list(map(int,input().split()))
ans = []
for i in range(n):
    ans.insert(i-nums[i], i+1)
print(*ans)