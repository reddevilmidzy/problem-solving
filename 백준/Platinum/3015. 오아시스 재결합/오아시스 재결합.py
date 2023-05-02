import sys
input = sys.stdin.readline

def solve():
    stk = []
    res = 0

    for num in nums:
        cnt = 1
        while stk and stk[-1][0] <= num:
            height, cnt = stk.pop()
            res += cnt
            cnt = 1 + (0 if height < num else cnt)
        if stk:
            res += 1
        stk.append((num, cnt))
    return res
n = int(input())
nums = [int(input()) for _ in range(n)]

print(solve())