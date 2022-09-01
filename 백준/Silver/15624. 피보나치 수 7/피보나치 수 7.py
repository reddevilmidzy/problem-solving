n=int(input())
dp = [0,1,1]
if n <= 2:
    print(dp[n])
else:
    for i in range(3,n+1):
        x=dp.pop()
        y=dp.pop()
        dp.append(x)
        dp.append((x+y)%1000000007)
    print(dp[-1])   