import sys
input = sys.stdin.readline

def solve(p_idx: int, s_idx: int) -> int:
    if dp[p_idx][s_idx] != -1:
        return dp[p_idx][s_idx]

    if p_idx < len(p) and s_idx < len(s) and p[p_idx] == s[s_idx]:
        dp[p_idx][s_idx] = solve(p_idx + 1, s_idx + 1)
        return dp[p_idx][s_idx]

    if p_idx == len(p):
        dp[p_idx][s_idx] = +(s_idx == len(s))
        return dp[p_idx][s_idx]

    if p[p_idx] == "*":
        if solve(p_idx + 1, s_idx) or (s_idx < len(s) and solve(p_idx, s_idx + 1)):
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