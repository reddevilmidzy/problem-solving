import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int,input().split()))
nums.sort()
ans = 0
st,ed = 0, n-1

while st < ed:
    tmp = nums[st] + nums[ed]
    if tmp < m:
        st += 1
    elif tmp > m:
        ed -= 1
    else:
        ans += 1
        st += 1
        ed -= 1 

print(ans)