import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

# 정렬 때린 후 이분탐색하면 될 것 같았으나
# 1, 4, 4, 7이 있을 때, k = 8 일때가 걸린다. 투포인터

left,right = 0, n-1
res = 0

while left <= right:
    if nums[right] >= k:
        res += 1
        right -= 1
    elif nums[left] + nums[right] >= k and left!=right:
        res += 1
        left += 1
        right -= 1
    else:
        left += 1

print(res if res else -1)