
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

mid_ans = []
right_ans = []
left_ans = []
# print(in_ord, un_ord)
for i in range(1,n-1):
    # 꿀통 중간에
    mid_ans.append(in_ord[i]+un_ord[i]-nums[0]-nums[-1])
    # 꿀통 우측 끝에
    right_ans.append(in_ord[-1]-nums[0]-nums[i]+(in_ord[-1]-in_ord[i]))
    # 꿀통 좌측 끝에
    left_ans.append(un_ord[0]-nums[-1]-nums[i]+(un_ord[0]-un_ord[i]))

print(max(max(mid_ans), max(right_ans), max(left_ans)))