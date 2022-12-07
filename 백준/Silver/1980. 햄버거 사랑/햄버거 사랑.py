n,m,t = map(int,input().split())

ans = [[0,t]]
for i in range(n, t+1, n):
    tmp = (t-i)//m + i//n
    coke = (t-i)%m
    ans.append([tmp, coke])

for j in range(m, t+1, m):
    tmp = (t-j)//n + j//m
    coke = (t-j)%n
    ans.append([tmp, coke])

ans.sort(key=lambda x: (x[1], -x[0]))
print(*ans[0])