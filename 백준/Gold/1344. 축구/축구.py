a=int(input())
b=int(input())

a/=100
b/=100
primes = {2,3,5,7,11,13,17}
m = 18

dp = [[[0]*(m+1) for _ in range(m+1)] for _ in range(m+1)]

# 둘다 득점 실패
dp[0][0][0] = (1-a)*(1-b)
dp[0][1][0] = a*(1-b)
dp[0][0][1] = (1-a)*b
dp[0][1][1] = a*b

for i in range(1, m+1):
    for j in range(m+1):
        for k in range(m+1):
            # 둘다 득점 못하는 경우의 수
            dp[i][j][k] = (1-a)*(1-b)*dp[i-1][j][k]
            
            if j:
                dp[i][j][k] += a*(1-b)*dp[i-1][j-1][k]
            if k:
                dp[i][j][k] += (1-a)*b*dp[i-1][j][k-1]
            if j and k:
                dp[i][j][k] += a*b*dp[i-1][j-1][k-1]

ans = 0

for i in range(m+1):
    for j in range(m+1):
        if i in primes or j in primes:
            ans += dp[m-1][i][j]

print(ans)