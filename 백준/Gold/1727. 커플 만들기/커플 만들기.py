import sys
input = sys.stdin.readline
INF = int(1e9)

def solve(a:list[int], b:list[int]) -> int:
    n = len(a)
    m = len(b)

    dp = [[INF]*(m+1) for _ in range(n+1)]

    dp[0][0] = 0

    for i in range(n):
        for j in range(min(m, i+1)):
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            dp[i+1][j+1] = min(dp[i][j] + abs(a[i]-b[j]), dp[i+1][j+1])

    return min([dp[i][m] for i in range(n+1)])

n,m = map(int,input().split())
boy = list(map(int,input().split()))
girl = list(map(int,input().split()))
boy.sort()
girl.sort()

if n==m:
    print(abs(sum(boy) - sum(girl)))
elif n < m:
    print(solve(girl, boy))
elif n > m:
    print(solve(boy, girl))