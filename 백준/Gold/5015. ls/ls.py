import sys
input = sys.stdin.readline

def solve(p_idx: int, s_idx: int) -> int:
    if dp[p_idx][s_idx] != -1:
        return dp[p_idx][s_idx]

    i = p_idx
    j = s_idx

    while i < len(p) and j < len(s) and p[i] == s[j]:
        i += 1
        j += 1

    if i == len(p):
        dp[p_idx][s_idx] = +(j == len(s))
        return dp[p_idx][s_idx]

    if p[i] == "*":
        for k in range(len(s) - j + 1):
            if solve(i + 1, j + k):
                dp[p_idx][s_idx] = 1
                return dp[p_idx][s_idx]
    dp[p_idx][s_idx] = 0
    return dp[p_idx][s_idx]

p = input().rstrip()
n = int(input())
m = 100
res = []
for _ in range(n):
    dp = [[-1]*(m + 1) for _ in range(m + 1)]
    s = input().rstrip()
    if solve(0, 0):
        res.append(s)

print(*res,sep='\n')