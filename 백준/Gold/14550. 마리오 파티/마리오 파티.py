import sys
input = sys.stdin.readline
INF = int(1e7)

def solve():
    dp = [[-INF]*(n+1) for _ in range(t)]
    dp[0][0] = 0
    for i in range(1, t):
        for j in range(n+1):
            for k in range(s, 0, -1):
                if j-k >= 0 and dp[i-1][j-k] != -INF and dp[i][j] < dp[i-1][j-k]+arr[j]:
                    dp[i][j] = dp[i-1][j-k] + arr[j]

    return max(dp[t-1][-s:])

while True:
    tmp = list(map(int,input().split()))
    if tmp[0] == 0: break
    n,s,t = tmp
    arr = [0]
    while len(arr) <= n:
        arr.extend(list(map(int,input().split())))
    print(solve())