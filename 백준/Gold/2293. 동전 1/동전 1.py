import sys
input = sys.stdin.readline

n,k=map(int,input().split())
coins=[]
ans = 0
for _ in range(n):
    coin=int(input())
    if coin<=k: coins.append(coin)

if coins == []:
    pass
else:
    dp=[0]*(k+1)
    for i in coins:
        dp[i] +=1
        for j in range(i, k+1):
            dp[j] += dp[j-i]
    ans = dp[k]

print(ans)