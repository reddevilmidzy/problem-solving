n = int(input())
nums = list(map(int,input().split()))

start = 0
end = n-1
res = []
while start < end:
    diff = nums[end]+nums[start]
    if diff>0:
        res.append((diff, nums[start], nums[end]))
        #heapq.heappush(res, (diff, nums[start], nums[end]))
        end -= 1
    elif diff<0:
        res.append((-diff, nums[start], nums[end]))
        #heapq.heappush(res, (-diff, nums[start], nums[end]))
        start += 1
    else:
        res.append((diff, nums[start], nums[end]))
        #heapq.heappush(res, (diff, nums[start], nums[end]))
        break
res.sort()
dist,a,b = res.pop(0)
print(a,b)