import sys
input = sys.stdin.readline

n=int(input())
road=list(map(str,input().rstrip()))
INF = int(1e9)

dp = [INF]*(n)
dp[0] = 0

after = 'BOJ'

for i in range(n):
    for j in range(i+1, n):
        if (after.index(road[i])+1)%3 == after.index(road[j]):
            # print(road[i], road[j])
            dp[j] = min(dp[j], dp[i]+(j-i)**2)
    
print(dp[n-1] if dp[n-1] != INF else -1)