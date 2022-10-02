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
    # 퇴사날 이후라면 무시
    if i+t_list[i]>n:
        continue
    # i번째 일을 하는 것과, 이전 작업을 하고 있는 것을 비교
    dp[i+t_list[i]] = max(res+p_list[i], dp[i+t_list[i]])

print(max(dp))