# 1~ n층까지 있다.
# k 개의 자리로 표현
# 1 ~ p 개를 반전
# 현재 X층에 있음

ans = 0

board = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
        [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
        [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
        [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
        [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
        [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
        [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
        [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
        [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
        [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]


def bt(s:list[int], p:int, val: list[int]):
    if len(s) == k:
        tmp = 0
        for i,j in enumerate(s):
            tmp += val[i][j]
        global ans
        if 1 <= tmp <= p and 1 <= int("".join(map(str,s))) <= n:
            ans += 1
        return 
    for i in range(10):
        s.append(i)
        bt(s, p, val)
        s.pop()

def solve(nums: list[int], p: int):
    res = [[] for _ in range(len(nums))]
    idx = 0
    for i in nums:
        for j in range(10):
            res[idx].append(board[i][j])
        idx += 1
    return res
n,k,p,x = map(int,input().split())
nums = list(map(int, str(x).zfill(k)))
res = solve(nums, p)
bt([], p, res)
print(ans)