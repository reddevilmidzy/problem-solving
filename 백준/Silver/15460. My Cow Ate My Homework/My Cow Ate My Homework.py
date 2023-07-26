INF = int(1e6)
n = int(input())
nums = list(map(int,input().split()))

pre_fix = [0]
min_val = [INF]*(n+1)

for i in range(n):
    pre_fix.append(pre_fix[-1] + nums[i])
    min_val[n-i-1] = min(min_val[n-i], nums[n-i-1])

ans = []
for i in range(1, n-1):
    ans.append((-(pre_fix[n] - pre_fix[i] - min_val[i])/(n-i-1), i))


ans.sort()
res = ans[0][0]

for i in range(n-2):
    if ans[i][0] == res:
        print(ans[i][1])
    else:
        break
