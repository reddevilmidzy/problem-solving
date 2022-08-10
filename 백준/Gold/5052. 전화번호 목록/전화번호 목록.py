import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = sorted([str(input().rstrip()) for i in range(n)])
    for j in range(n-1):
        if len(nums[j]) < len(nums[j+1]):
            if nums[j]==nums[j+1][:len(nums[j])]:
                print('NO')
                break
    else:
        print('YES')