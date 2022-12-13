import sys
input = sys.stdin.readline

n,s,r = map(int, input().split())
broke = list(map(int,input().split()))
redun = list(map(int,input().split()))
broke, redun = list(set(broke)-set(redun)), list(set(redun)-set(broke))

ans = 0
for i in broke:
    if i-1 in redun:
        redun.remove(i-1)
    elif i+1 in redun:
        redun.remove(i+1)
    else:
        ans += 1

print(ans)