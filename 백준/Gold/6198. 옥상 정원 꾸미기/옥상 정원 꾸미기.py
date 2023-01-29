import sys
input = sys.stdin.readline

n = int(input())
high = [int(input()) for _ in range(n)]

res = []
stk = []

for i in range(n-1,-1,-1):
    cnt = 0
    while stk:
        if stk[-1][0] < high[i]:
            cnt += stk.pop()[1] + 1
        else:
            stk.append([high[i], cnt])
            break
    if not stk:
        stk.append([high[i], cnt])

    res.append(cnt)

print(sum(res))