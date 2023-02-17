def is_possible(n, times, target):
    res = 0
    for time in times:
        res += target//time
    
    return res >= n


def solution(n, times):
    times.sort()
    ans = []
    st, ed = 0, n*times[-1]
    while st <= ed:
        mid = (st + ed) // 2
        if is_possible(n, times, mid):
            ans.append(mid)
            ed = mid - 1
        else:
            st = mid + 1
    return min(ans)

