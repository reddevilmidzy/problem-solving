import sys
input = sys.stdin.readline
cnt = 0
user = {}
for i in range(int(input().rstrip())):
    s = input().rstrip()
    if s == "ENTER":
        cnt += sum(user.values())
        user = {}
    else:
        if s not in user: user[s] = 1
        else: pass
cnt += sum(user.values())

print(cnt)