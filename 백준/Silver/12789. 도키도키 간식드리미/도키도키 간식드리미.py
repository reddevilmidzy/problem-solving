import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
stk = []
idx = 0

for i in range(n):
    if idx + 1 == nums[i]:
        idx = nums[i]
    elif stk:
        while stk and idx + 1 == stk[-1]:
            idx = stk.pop()
        if not stk or stk[-1] > nums[i]:
            stk.append(nums[i])
        else:
            print("Sad")
            break
    else:
        stk.append(nums[i])
else:
    while stk and idx + 1 == stk[-1]:
        idx = stk.pop()
    
    if not stk:
        print("Nice")
    else:
        print("Sad")