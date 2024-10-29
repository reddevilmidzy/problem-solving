def solution(N, number):
    ans = 0
    m = (10**6)
    INF = float('inf')
    dp = [INF for _ in range(m + 1)]

    tmp = N
    cnt = 1
    dp[1] = 2
    arr = []
    while tmp <= m:
        dp[tmp] = cnt
        arr.append((tmp, cnt))
        tmp = tmp * 10 + N
        cnt += 1

    for i in range(1, 100000+1):

        if dp[i] == INF: continue
        dp[i+1] = min(dp[i+1], dp[i] + 2)
        dp[i-1] = min(dp[i-1], dp[i] + 2)
        for j, k in arr:
            if i // j >= 1:
                dp[i // j] = min(dp[i] + k, dp[i // j])
            if i - j >= 1:
                dp[i - j] = min(dp[i] + k, dp[i - j])
            if i + j <= m:
                dp[i + j] = min(dp[i] + k, dp[i + j])
            if i * j <= m:
                dp[i * j] = min(dp[i] + k, dp[i * j])

    for i in range(1, 100000+1):

        if dp[i] >= 11: continue

        dp[i+1] = min(dp[i] + 2, dp[i+1])
        dp[i-1] = min(dp[i-1], dp[i] + 2)
        for j, k in arr:
            if i // j >= 1:
                dp[i // j] = min(dp[i] + k, dp[i // j])
            if i - j >= 1:
                dp[i - j] = min(dp[i] + k, dp[i - j])
            if i + j <= m:
                dp[i + j] = min(dp[i] + k, dp[i + j])
            if i * j <= m:
                dp[i * j] = min(dp[i] + k, dp[i * j])

    return dp[number] if dp[number] <= 8 else -1