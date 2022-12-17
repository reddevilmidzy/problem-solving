import sys, math
input = sys.stdin.readline
for _ in range(int(input())):
    tmp = list(map(int,input().split()))
    n = tmp[0]
    nums = tmp[1:]
    ans = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            ans += math.gcd(nums[i], nums[j])
    print(ans)