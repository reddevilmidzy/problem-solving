import sys
input = sys.stdin.readline

n = int(input())
res = []
for _ in range(n):
    paper = input().rstrip()
    ans = ''
    for i in paper:
        if i.isnumeric():
            ans += i
        elif not i.isnumeric() and ans != '':
            res.append(int(ans))
            ans = ''
    if ans != '':
        res.append(int(ans))
print(*sorted(res), sep='\n')