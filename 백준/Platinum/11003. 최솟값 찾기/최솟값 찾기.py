from heapq import heappush, heappop
n,l = map(int,input().split())
nums = list(map(int,input().split()))
val_hq = []

ans = [0]*n

for idx,val in enumerate(nums):
    if len(val_hq) < l:
        heappush(val_hq, (val, idx))
        min_val, min_idx = val_hq[0]
        ans[idx] = min_val
    else:
        heappush(val_hq, (val, idx))        
        while val_hq[0][1] <= idx - l:
            heappop(val_hq)
        
        ans[idx] = val_hq[0][0]
print(*ans)