import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0
# 최악의 케이스
if n==k:
    print(0)
    exit()
pre = []
for i in range(n-1):
    pre.append(nums[i+1]-nums[i])
pre.sort(reverse=True)
print(sum(pre[k-1:n]))