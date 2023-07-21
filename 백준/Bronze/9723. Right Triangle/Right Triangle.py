import sys
input = sys.stdin.readline

t = int(input())
YES = "YES"
NO = "NO"
for i in range(1,t+1):
    nums = sorted(list(map(int,input().split())))
    print(f"Case #{i}: {YES if nums[0]**2+nums[1]**2==nums[2]**2 else NO}")