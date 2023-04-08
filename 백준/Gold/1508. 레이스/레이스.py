# 가장 가까운 심판의 거리가 최대가 되는 값을 이진탐색으로 찾고,
# 해당 위치를 리턴

def is_can_be_min_dist(dist: int) -> bool:
    cnt = 1
    pre = 0
    for i in range(1, k):
        if nums[i] - nums[pre] >= dist: # 차이가 설정한 최소보다 클때
            pre = i
            cnt += 1
        if cnt >= m:
            return True
    return False

def set_judge(dist: int):
    res = [1]
    pre = 0
    cnt = 1
    for i in range(1, k):
        if nums[i] - nums[pre] >= dist:
            if cnt >= m:
                res.extend([0]*(k - len(res)))
                return res
            cnt += 1
            res.append(1)
            pre = i
        else:
            res.append(0)
    return res

n,m,k = map(int,input().split()) # 레이스 길이, 심판수, 심판 위치 시킬수 있는 위치
nums = list(map(int,input().split()))

left, right = 1, nums[-1]
dist = 1

while left <= right:
    mid = (left + right) // 2

    if is_can_be_min_dist(mid):
        dist = mid
        left = mid + 1
    else:
        right = mid - 1

print(*set_judge(dist), sep='')