MOD = int(1e6)
m = "-"+input().rstrip()
n = len(m)
dp = [0]*(n+1)

dp[0] = +(m[1] != "0")
dp[1] = +(m[1] != "0")

for i in range(2, n):
    if m[i] != "0":
        dp[i] = dp[i-1]
    if m[i-1] != "0" and 0 < int(m[i-1]+m[i]) <= 26:
        dp[i] += dp[i-2]
    dp[i] %= MOD

print(dp[-2])