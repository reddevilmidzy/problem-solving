import sys
input = sys.stdin.readline

n = int(input())
t_list = []
p_list = []
dp = [0 for _ in range(n+1)]
for _ in range(n):
    t,p = map(int,input().split())
    t_list.append(t)
    p_list.append(p)

res = -1
for i in range(n):
    res = max(res, dp[i])
    if i+t_list[i]<=n:
        dp[i+t_list[i]] = max(res+p_list[i], dp[i+t_list[i]])
print(max(dp))