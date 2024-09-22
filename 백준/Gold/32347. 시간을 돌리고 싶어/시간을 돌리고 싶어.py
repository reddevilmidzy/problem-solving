import sys
input = sys.stdin.readline

def solve(target: int) -> bool:

    cnt = 0 # 사용횟수
    cur = n - 1
    visited = [False] * n

    while cur < n and cnt <= k:
        if cur <= 0:
            return cnt <= k
        if nums[cur] and not visited[max(0, cur-target)]:
            cur -= target
            visited[max(0, cur)] = True
            cnt += 1
        elif cur + 1 < n and not visited[cur + 1]:
            cur += 1
            visited[cur] = True
        else:
            return False

    return cur <= 0 and cnt <= k


n,k = map(int,input().split())
nums = list(map(int,input().split()))

st = 1
ed = n+1
res = n-1
while st <= ed:
    mid = (st + ed) // 2
    if solve(mid):
        res = mid
        ed = mid - 1
    else:
        st = mid + 1

print(res)