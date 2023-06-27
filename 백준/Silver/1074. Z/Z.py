n,r,c= map(int,input().split()) # r 세로
check = 2**(n-1)
ans = 0
plus = 4**(n-1)
while n:
    if r < check and c < check:
        ans += plus*0
    elif r < check and c >= check:
        ans += plus*1
        c -= check
    elif r >= check and c < check:
        ans += plus*2
        r -= check
    elif r >= check and c >= check:
        ans += plus*3
        r -= check
        c -= check
    n -= 1
    check = 2**(n-1)
    plus = 4**(n-1)
print(ans)