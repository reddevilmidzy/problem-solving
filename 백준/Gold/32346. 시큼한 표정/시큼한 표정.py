import sys, math
input = sys.stdin.readline
MOD = int(1e9) + 7

n = int(input())
s = input().rstrip()

# 10, 01, 1100, 1010, 0011, 0101, 1001, 0110
spot = [] # >< 의 뿌리

for i in range(n-1):
    if s[i]==">" and s[i+1]=="<":
        idx = 0
        while i-idx >= 0 and i+1+idx<n:
            if s[i-idx] == ">" and s[i+1+idx] == "<":
                spot.append((i-idx,i+1+idx)) # length
                idx +=1
            else:
                break

nums = []

for x,y in spot:
    left = x
    right = n - y - 1
    tot = left + right
    nums.append(math.comb(tot, left) % MOD)
print(sum(nums)%MOD)
