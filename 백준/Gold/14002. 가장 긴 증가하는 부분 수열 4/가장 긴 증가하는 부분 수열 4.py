n = int(input())
nums = list(map(int,input().split()))
dp = [1]*n
route = [i for i in range(n)]

for i in range(n):
    for j in range(i,-1,-1):
        if nums[j] < nums[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            route[i] = j
node = dp.index(max(dp))
ans = [nums[node]]

while node != route[node]:
    node = route[node]
    ans.append(nums[node])
print(max(dp))
print(*ans[::-1])