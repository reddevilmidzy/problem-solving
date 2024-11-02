import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

one = 0
two = 1
ss = {nums[one]}
res = 1
while two < n:
    if nums[two] not in ss:
        ss.add(nums[two])
        two += 1
        res += two - one
    else:
        ss.remove(nums[one])
        one += 1
print(res)
