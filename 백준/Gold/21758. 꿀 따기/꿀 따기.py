import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

in_ord = [nums[0]]
un_ord = [nums[-1]]

for i in range(1,n):
    in_ord.append(in_ord[i-1]+nums[i])
    un_ord.append(un_ord[i-1]+nums[n-i-1])

un_ord = list(reversed(un_ord))

mid_ans = 0
right_ans = 0
left_ans = 0
for i in range(1,n-1):
    mid_ans = max(mid_ans, in_ord[i]+un_ord[i]-nums[0]-nums[-1])
    right_ans = max(right_ans, in_ord[-1]-nums[0]-nums[i]+(in_ord[-1]-in_ord[i]))
    left_ans = max(left_ans, un_ord[0]-nums[-1]-nums[i]+(un_ord[0]-un_ord[i]))
print(max(mid_ans, right_ans, left_ans))