import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
obn = [-1]*n
stk = []

for i in range(n):
    while stk and nums[stk[-1]] < nums[i]:
        obn[stk.pop()] = nums[i]
    stk.append(i)

print(*obn, sep=' ')