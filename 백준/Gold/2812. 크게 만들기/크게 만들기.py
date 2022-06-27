import sys
input = sys.stdin.readline

n,k = map(int,input().split())
num = list(map(int,input().rstrip()))
ans = []
check = k

for i in range(n):
    while len(ans) > 0 and check > 0:
        if ans[-1] < num[i]:
            ans.pop()
            check -= 1
        else:
            break
    ans.append(num[i])

print(*ans[:n-k],sep='')