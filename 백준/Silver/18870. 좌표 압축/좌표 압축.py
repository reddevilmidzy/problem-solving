n = int(input())
num = list(map(int, input().split()))

check = list(set(num.copy()))
check.sort()

coor = dict()
idx = 0
for i in check:
    coor[i] = idx
    idx += 1

for j in num:
    print(coor[j], end=" ")