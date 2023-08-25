import math
n = int(input())
nums = [int(input()) for _ in range(n)]
diff = [nums[i+1] - nums[i] for i in range(n-1)]
gcd = math.gcd(*diff)
print(sum([i//gcd for i in diff])-n+1)