import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(8)]
tmp = sorted(nums, reverse=True)
print(sum(tmp[:5]))
ans = sorted([nums.index(tmp[i])+1 for i in range(5)])
print(*ans)