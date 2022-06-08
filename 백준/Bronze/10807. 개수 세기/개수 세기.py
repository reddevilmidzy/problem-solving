n = int(input())
nums = list(map(int,input().split()))
target = int(input())
cnt = 0
for num in nums:
    if num == target:
        cnt += 1
print(cnt)