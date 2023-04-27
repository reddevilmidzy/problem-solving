import sys
input = sys.stdin.readline

def collocate(mid: int, q: int) -> bool:
    pre = 0
    cnt = 0
    for cur in positions:
        if cur - pre >= mid:
            cnt += 1
            pre = cur
    return cnt > q

def solve(q:int) -> int:
    st,ed = 1, l
    ans = -1
    while st<=ed:
        mid = (st+ed) // 2
        if collocate(mid, q):
            ans = mid
            st = mid + 1
        else:
            ed = mid - 1
    return ans

n,m,l = map(int,input().split())
positions = [int(input()) for _ in range(m)] + [l]

for _ in range(n):
    q = int(input())
    print(solve(q))