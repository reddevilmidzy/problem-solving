import sys
input = sys.stdin.readline
# input = open("input.txt", "r").readline
n,m = map(int,input().split())
nums = [list(map(int,input().rstrip())) for _ in range(n)]
pre = [[0]*(m+1) for _ in range(n+1)]
ans = []

# print(*nums, sep='\n')
# 누적합 배열 만들기
for r in range(1, n+1):
    for c in range(1, m+1):
        pre[r][c] = pre[r-1][c] + pre[r][c-1] - pre[r-1][c-1] + nums[r-1][c-1]

#  가로로 3개 나누기

# print("가로")
for i in range(1,m):
    for j in range(i+1, m):
        ans.append(pre[n][i] * (pre[n][j] - pre[n][i]) * (pre[n][m] - pre[n][j]))
        # print(pre[n][i] , (pre[n][j] - pre[n][i]) , (pre[n][m] - pre[n][j]))

# print("세로")
# 세로로 3개 나누기
for i in range(1, n):
    for j in range(i+1, n):
        ans.append(pre[i][m] * (pre[j][m] - pre[i][m]) * (pre[n][m] - pre[j][m]))
        # print(pre[i][m] * (pre[j][m] - pre[i][m]) * (pre[n][m] - pre[j][m]))

# print("사각형")
# 직사각형 4개로 나누기
for i in range(1,n):
    for j in range(1,m):
        q1 = pre[i][m] - pre[i][j]
        q2 = pre[i][j]
        q3 = pre[n][j] - pre[i][j]
        q4 = pre[n][m] + pre[i][j] - pre[n][j] - pre[i][m]
        # print(q1, q2, q3, q4)

        ans.append((q1+q2)*q3*q4)
        ans.append(q1*(q2+q3)*q4)
        ans.append(q1*q2*(q3+q4))
        ans.append(q2*q3*(q4+q1))

# print(ans)
print(max(ans))