n = int(input())
nums = list(map(int,input().split()))
speed = nums[-1]

for i in range(n-2, -1, -1):
    if nums[i] > speed:
        speed = nums[i]
    else:
        if speed%nums[i]:
            speed = (speed//nums[i]+1) *nums[i]
print(speed)