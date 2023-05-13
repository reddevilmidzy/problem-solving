import sys
input = sys.stdin.readline

n = int(input())
nums = reversed([int(input()) for _ in range(n)])
last = n
ans = 0
for num in nums:
    if last == num:
        last -= 1
    else:
        ans += 1
print(ans)