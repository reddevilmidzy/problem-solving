# 1~ n층까지 있다.
# k 개의 자리로 표현
# 1 ~ p 개를 반전
# 현재 X층에 있음

ans = []

def bt(s:list[int], p:int, val: list[int]):
    if len(s) == k:
        tmp = 0
        for i,j in enumerate(s):
            tmp += val[i][j]
        if 1 <= tmp <= p and 1 <= int("".join(map(str,s))) <= n:
            ans.append(s[::])
        return 
    for i in range(10):
        s.append(i)
        bt(s, p, val)
        s.pop()

def diff(a: int, b: int) -> int:
    a = disit[a]
    b = disit[b]
    res = 0
    for i,j in zip(a,b):
        if i != j:
            res += 1
    return res

def solve(nums: list[int], p: int):
    res = [[] for _ in range(len(nums))]
    idx = 0
    for i in nums:
        for j in range(10):
            res[idx].append((diff(i,j)))
        idx += 1
    return res

n,k,p,x = map(int,input().split())
nums = list(map(int, str(x).zfill(k)))
disit = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
res = solve(nums, p)
bt([], p, res)
print(len(ans))