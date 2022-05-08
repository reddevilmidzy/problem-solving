import sys
input = sys.stdin.readline
body = []
n = int(input().rstrip())
for i in range(n):
    weight, height = map(int, input().rstrip().split())
    a = [weight, height, i]
    body.append(a)
body.sort()
rank = 0
result = []
for j in range(n-1):
    for k in range(j+1, n):
        if body[j][0] < body[k][0] and body[j][1] < body[k][1]:
            rank += 1
    result.append([body[j][2], rank+1])
    rank = 0
result.append([body[-1][2], 1])
result.sort()
for l in result:
    print(l[1], end=" ")