MOD = int(1e9)
MAX = 1<<10
n = int(input())
m = 10

def solve():
    dp = [[[0]*(MAX) for _ in range(m)] for _ in range(n+1)]

    for i in range(1,m):
        dp[1][i][1<<i] = 1

    for length in range(1, n+1):
        for ed in range(m):
            for bit in range(MAX):
                if ed == 0:
                    dp[length][ed][bit | (1 << ed)] += dp[length-1][ed+1][bit]
                elif ed == 9:
                    dp[length][ed][bit | (1 << ed)] += dp[length-1][ed-1][bit]
                else:
                    dp[length][ed][bit | (1 << ed)] += dp[length-1][ed-1][bit] + dp[length-1][ed+1][bit]

                dp[length][ed][bit | (1 << ed)] %= MOD

    return sum(dp[n][i][MAX-1] for i in range(m))%MOD
print(solve())