import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())
# print(s,t)
while True:
    if len(s) == len(t):
        if s == t:
            print(1)
            break
        else:
            print(0)
            break

    check = t.pop()
    if check == 'A':
        pass
    else:
        t.reverse()