import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

nums = [[a[i], b[i]] for i in range(n)]
nums.sort(key=lambda x:(x[-1], x[0]))
# 30 일 씩 증가를 최소로 
# 기한이 가장 적게 남은 깊콘만 사용 가능
# 기한이 지날 것 같아 값을 올려버리면 쓸 수 없을 수도 있을 듯

res = 0
pre = nums[0][1]
cur_max = nums[0][0]

for i in range(n):
    if nums[i][0] < pre:
        cnt = (pre - nums[i][0] + 29) // 30
        nums[i][0] += 30 * cnt
        res += cnt
    
    cur_max = max(cur_max, nums[i][0])
    if nums[i][1] != nums[min(n-1, i+1)][1]: 
        pre = max(cur_max, nums[i+1][1])

# print(nums)

print(res)