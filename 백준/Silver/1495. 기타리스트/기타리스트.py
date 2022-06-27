n, s, m = map(int, input().split())
v = list(map(int, input().split()))

# dp 정의
# 행에는 최대볼륨 열에는 곡의 개수
dp = [[0] * (m+1) for i in range(n+1)]

dp[0][s] = 1

for i in range(1, n+1): # 곡의 개수만큼
    for j in range(m+1): # 최대 볼륨
        if dp[i-1][j] != 0: # 볼륨 조절 가능하다면
            # print(dp[i-1][j])
            if 0<=j+v[i-1]<=m: 
                dp[i][j+v[i-1]]=1 
            if 0<=j-v[i-1]<=m: 
                dp[i][j-v[i-1]]=1

# 볼륨 조절 불가한 경우 -1 출력을 위해 초기값 
ans = -1 
dp = dp[n]
# 최대값 찾기 위해 내림차순으로 for 문
for i in range(m, -1, -1):
    if dp[i]==1: 
        ans = i 
        break 
print(ans)