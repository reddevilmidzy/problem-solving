n,m = map(int,input().split())
nums = list(map(int,input().split()))

neg = [abs(num) for num in nums if num < 0]
pos = [num for num in nums if num > 0]
pos.sort(reverse=True)
neg.sort(reverse=True)
candy = []
for i in range(0, len(neg), m):
    candy.append(neg[i])
for i in range(0, len(pos), m):
    candy.append(pos[i])

print(sum(candy)*2 - max(candy))