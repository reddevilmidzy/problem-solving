import sys
n=int(input())
nums=list(map(int,input().split()))
dp=[1]+[0]*6
for i in range(n):
    tmp=[0]*7
    for j in range(7):
        if dp[j]:
            tmp[j]=1
            tmp[(j+nums[i]%7)%7]=1
    if tmp[4]:
        print("YES")
        exit()
    dp=tmp
print("NO")