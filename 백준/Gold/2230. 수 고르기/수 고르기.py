import sys
input = sys.stdin.readline

def two_pointer() -> int:
    one,two = 0,0
    res = []
    while one <= two and two < n:
        min_res = nums[two] - nums[one]
    
        if min_res == m:
            res.append(min_res)
            return min_res
        elif min_res > m:
            res.append(min_res)
            one += 1
        elif min_res < m:
            two += 1
    return min(res)

n,m = map(int,input().split())
nums = sorted([int(input()) for _ in range(n)])

print(two_pointer())