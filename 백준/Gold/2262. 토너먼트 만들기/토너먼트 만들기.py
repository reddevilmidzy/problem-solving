int(input())
nums = list(map(int,input().split()))
ans = 0
for val, idx in sorted([(val,idx) for idx,val in enumerate(nums)],reverse=1):
    cur = nums.index(val)
    pre = max(cur-1, 0)
    suf = min(cur+1, len(nums)-1)
    ans += [max,min][suf-pre==2](val-nums[pre], val-nums[suf])
    nums.remove(val)
print(ans)