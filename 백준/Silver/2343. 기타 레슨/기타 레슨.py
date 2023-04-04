import sys
input = sys.stdin.readline

def can_record(limit: int) -> bool:
    tmp = 0
    cnt = 1
    for num in nums:
        if tmp + num <= limit:
            tmp += num
        elif num <= limit:
            cnt += 1
            tmp = num
        else:
            return False
    return cnt <= m

n,m = map(int,input().split())
nums = list(map(int,input().split()))

left, right = 1, sum(nums)

while left <= right:
    mid = (left + right) // 2
    if can_record(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)