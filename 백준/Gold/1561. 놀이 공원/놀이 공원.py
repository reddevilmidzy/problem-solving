import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # n명의 아이들, m종류
nums = list(map(int,input().split()))

if n <= m:
    print(n)
    exit()

# t 초가 지났을 때 
def can_ride(time: int) -> bool:
    res = 0
    for i in range(m):
        res += time//nums[i] + 1
    return res

left, right = 0, sys.maxsize

while left <= right:
    mid = (left + right) // 2
    if can_ride(mid) >= n: # n명이상 탑승 
        right = mid - 1
    else:
        left = mid + 1

# left = n명 탑승 할 수 있는 최소 시간
# 직전에 비어있는 놀이 기구 타면 됨
order = n - can_ride(left-1)
for i in range(m):
    if left % nums[i] == 0:
        order -= 1
        if order == 0:
            print(i+1)
            break