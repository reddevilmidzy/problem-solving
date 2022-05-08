import sys
input = sys.stdin.readline
body = []
n = int(input().rstrip())
for i in range(n):
    body.append([*map(int, input().rstrip().split()), i])
# print(body)
body.sort()
result = []
for j in range(n-1):
    rank = 0
    for k in range(j+1, n):
        if body[j][0] < body[k][0] and body[j][1] < body[k][1]:
            rank += 1
    result.append([body[j][2], rank+1])
result.append([body[-1][2], 1])
for l in sorted(result):
    print(l[1], end=" ")