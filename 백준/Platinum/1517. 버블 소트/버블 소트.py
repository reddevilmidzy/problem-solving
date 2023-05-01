def merge_sort(nums: list[int]) -> list[int]:
    global ans
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    l_idx, r_idx = 0,0
    res = []
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            res.append(left[l_idx])
            l_idx += 1
        else:
            ans += mid - l_idx
            res.append(right[r_idx])
            r_idx += 1
    res.extend(left[l_idx:])
    res.extend(right[r_idx:])
    return res

n = int(input())
nums = list(map(int,input().split()))
ans = 0
merge_sort(nums)
print(ans)