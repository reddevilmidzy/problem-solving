import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    nums = sorted(list(map(int,input().split())))
    print(f"Scenario #{i}:")
    print(["no","yes"][nums[-1]**2 == nums[0]**2 + nums[1]**2])
    print()