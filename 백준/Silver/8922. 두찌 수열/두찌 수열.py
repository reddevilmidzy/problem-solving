import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    cnt = 0
    while cnt < 100:
        tmp = [[] for _ in range(n)]
        for i in range(n):
            tmp[i] = abs(nums[i] - nums[i-1])
        
        nums = tmp
        cnt += 1
    print("ZERO" if sum(tmp) == 0 else "LOOP")