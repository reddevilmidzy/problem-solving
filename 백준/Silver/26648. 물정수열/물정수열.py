def solve():
    n,m = int(input()),3
    nums = [list(map(int,input().split())) for _ in range(m)]
    pre = min(nums[0][0], nums[1][0], nums[2][0])
    for i in range(1,n):
        tmp = sorted(nums[j][i] for j in range(m))
        if tmp[2] <= pre:
            return "NO"
        elif tmp[0] > pre:
            pre = tmp[0]
        else:
            pre += 1
    return "YES"
print(solve())