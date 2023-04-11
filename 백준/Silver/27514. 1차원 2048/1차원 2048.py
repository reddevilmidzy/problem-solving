n = int(input())
nums = list(map(int,input().split()))

two = dict()

for i in range(0, 63):
    two[2**i] = 0

for num in nums:
    if num:
        two[num] += 1

for i in range(0, 62):
    if two[2**i] > 0:
        two[2**(i+1)] += two[2**i]//2

ans = 0

for i in range(62, -1, -1):
    if two[2**i] > 0:
        ans = 2**i
        break
print(ans)