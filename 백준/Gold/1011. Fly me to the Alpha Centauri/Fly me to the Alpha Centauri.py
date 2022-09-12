import sys
input = sys.stdin.readline
res = []
for _ in range(int(input())):
    x,y = map(int,input().split())
    dist = y-x
    n = int(dist**0.5)
    ans = 2*n-1
    if dist -n**2 == 0:
        pass
    elif dist - n**2 <= n:
        ans +=1
    else:
        ans += 2
    res.append(ans)
print(*res, sep='\n')