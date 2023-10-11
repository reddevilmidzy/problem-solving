import sys
input = sys.stdin.readline

n = int(input())
res = 0
neg = []
pos = []
zero = False

for _ in range(n):
    num = int(input())
    if num < 0:
        neg.append(num)
    elif num > 1:
        pos.append(num)
    elif num == 1:
        res += 1
    else:
        zero = True
neg.sort()
if len(neg)%2:
    if zero:
        neg.append(0)
    else:
        neg.append(1)
pos.append(1)
pos.sort(reverse=True)
for i in range(0,len(neg)-1,2):
    res += neg[i]*neg[i+1]

for i in range(0, len(pos)-1, 2):
    res += pos[i]*pos[i+1]
print(res)