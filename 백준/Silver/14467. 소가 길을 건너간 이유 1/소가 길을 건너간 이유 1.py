import sys
input = sys.stdin.readline
cow = dict()
cnt = 0
for i in range(int(input())):
    n, pos = map(int,input().split())
    if n not in cow:
        cow[n] = pos
    else:
        if cow[n] != pos:
            cnt += 1
            cow[n] = pos
print(cnt)