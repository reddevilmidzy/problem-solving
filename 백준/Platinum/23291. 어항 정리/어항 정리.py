n,k = map(int,input().split())
nums = list(map(int,input().split()))

def plus(nums):
    min_fish = min(nums)
    for i in range(n):
        if nums[i] == min_fish:
            nums[i] += 1
    return nums

def stack(lis):
    res = [[lis[0]],lis[1:]]
    while True:
        if len(res) > len(res[-1]) - len(res[0]):break
        idx = len(res[0])
        tmp = []
        for i in range(len(res)):tmp.append(res[i][:idx])
        turned = turn(tmp)
        res = turned[::] + [res[-1][idx:]]
    return res

def condi(lis):
    n = len(lis)
    res = [[0]*len(lis[i]) for i in range(n)]
    for i in range(len(res)):
        for j in range(len(res[i])):
            if j != 0 and abs(lis[i][j] - lis[i][j-1])//5 > 0:
                if lis[i][j] < lis[i][j-1]:
                    res[i][j] += abs(lis[i][j] - lis[i][j-1])//5
                    res[i][j-1] -= abs(lis[i][j] - lis[i][j-1])//5
                else:
                    res[i][j] -= abs(lis[i][j] - lis[i][j-1])//5
                    res[i][j-1] += abs(lis[i][j] - lis[i][j-1])//5
            if i != 0 and len(lis[i-1]) > j and abs(lis[i][j] - lis[i-1][j])//5 > 0:
                if lis[i][j] < lis[i-1][j]:
                    res[i][j] += abs(lis[i][j] - lis[i-1][j])//5
                    res[i-1][j] -= abs(lis[i][j] - lis[i-1][j])//5
                else:
                    res[i][j] -= abs(lis[i][j] - lis[i-1][j])//5
                    res[i-1][j] += abs(lis[i][j] - lis[i-1][j])//5
    
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] += lis[i][j]
    return res

def turn(lis):
    n, m = len(lis), len(lis[0])
    res = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            res[j][n - i - 1] = lis[i][j]
    return res

def rematch(lis):
    res = []
    n,m = len(lis), len(lis[-1])
    for j in range(m):
        for i in range(n - 1, -1, -1):
            if len(lis[i]) > j:
                res.append(lis[i][j])
    return res

def levitate(lis):
    n = len(lis)
    tmp = [lis[:n//2][::-1], lis[n//2:]]
    return [tmp[-1][:n//4][::-1], tmp[0][:n//4][::-1], tmp[0][n//4:], tmp[-1][n//4:]]

ans = 0
while max(nums) - min(nums) > k:
    nums = rematch(condi(levitate(rematch(condi(stack(plus(nums)))))))
    ans += 1
print(ans)