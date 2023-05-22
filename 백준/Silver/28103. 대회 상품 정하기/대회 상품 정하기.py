n,m,x = map(int,input().split())
nums = list(map(int,input().split()))
ans = [0]*m

for i in range(m-1):
    ans[i] = min(n, (x-n*nums[-1])//(nums[i]-nums[-1]))
    n -= ans[i]
    x -= nums[i]*ans[i]
ans[m-1] = n
print(*ans)