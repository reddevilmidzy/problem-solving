import sys
input = sys.stdin.readline

def solution(n, d, nums):
    prefix = [0]*(n+1)
    ans = [0]*(d+1)
    for i in range(1, n+1):
        prefix[i] = (nums[i-1] + prefix[i-1]) % d
        ans[prefix[i]] += 1
    res = ans[0]
    for i in range(d):
        res += ans[i] * (ans[i] - 1) // 2
    return res

for _ in range(int(input())):
    d, n = map(int,input().split())
    nums = list(map(int,input().split()))
    print(solution(n,d,nums))