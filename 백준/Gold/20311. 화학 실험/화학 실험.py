import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))

def solve():
    for num in nums:
        if num > k: return [-1]
    
    tmp = [[nums[i], i+1] for i in range(k)]
    tmp.sort(key=lambda x:-x[0])
    res = [0]*n
    idx = 0
    for i in range(0, n, 2):
        if tmp[idx][0] <= 0:
            idx += 1
        tmp[idx][0] -= 1
        res[i] = tmp[idx][1]
    for i in range(1, n, 2):
        if tmp[idx][0] <= 0:
            idx += 1
        tmp[idx][0] -= 1
        res[i] = tmp[idx][1]
        
    return res

print(*solve())
