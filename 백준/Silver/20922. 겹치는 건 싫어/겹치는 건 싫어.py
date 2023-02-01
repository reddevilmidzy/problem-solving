import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))

arr = [0]*(max(nums)+1)
ans = 1
one,two = 0,0

while two < n:
    
    if arr[nums[two]] < k:
        arr[nums[two]] += 1
        two += 1
    else:
        arr[nums[one]] -= 1
        one += 1
    ans = max(ans, two-one)
print(ans)