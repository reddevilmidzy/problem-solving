from collections import Counter
n,x = map(int,input().split())
nums = list(map(int,input().split()))

window = sum(nums[:x])
ans = [window]
pre = 0

for i in range(x, n):
    window += nums[i] - nums[pre]
    pre += 1
    ans.append(window)

ans = Counter(ans)
if max(ans.keys()) != 0:
    print(max(ans.keys()), ans[max(ans.keys())], sep='\n')
else:
    print("SAD")