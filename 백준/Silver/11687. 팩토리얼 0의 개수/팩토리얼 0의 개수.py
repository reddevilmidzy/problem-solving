m = int(input())

def cnt(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros

left, right= 1, m * 5
res = 0

while left <= right:
    mid = (left + right) // 2
    zero_count = cnt(mid)
    if zero_count < m:
        left = mid + 1
    else:
        right = mid - 1
        res = mid

print(res if cnt(res) == m else -1)