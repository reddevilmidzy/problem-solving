import sys
input = sys.stdin.readline

def solve():
    left, right = 0, n-1
    res = sys.maxsize

    for left in range(n-2):
        for right in range(n-1,left+2,-1):
            res = min(res, two_point(nums[left]+nums[right], left, right))
            if not res:
                return res
    return res

def two_point(elsa: int, left: int, right: int) -> int:
    st, ed = left + 1, right - 1
    res = sys.maxsize

    while st <= ed:
        anna = nums[st] + nums[ed]
        res = min(res, abs(anna - elsa))
        if anna < elsa:
            st += 1
        elif anna > elsa:
            ed -= 1
        else:
            break
    return res

n = int(input())
nums = sorted(list(map(int,input().split())))

print(solve())