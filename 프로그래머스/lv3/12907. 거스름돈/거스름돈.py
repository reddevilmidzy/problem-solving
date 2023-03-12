
def solution(n, money):
    mod = int(1e9)+7
    money.sort()
    dp = [0]*(n+1)
    for i in money:
        dp[i] += 1
        for j in range(i+1, n+1):
            dp[j] += dp[j-i]%mod
    return dp[n]
