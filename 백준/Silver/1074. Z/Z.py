n,r,c= map(int,input().split()) # r 세로

check = 2**(n-1)
ans = 0
plus = 4**(n-1)
while n:
    #print('n',n,'r',r,'c',c,'check',check)
    if r < check and c < check:
        ans += plus*0
        #print('행보',0)
    elif r < check and c >= check:
        ans += plus*1
        c -= check
        #print('행보',1)
    elif r >= check and c < check:
        ans += plus*2
        r -= check
        #print('행보',2)
    elif r >= check and c >= check:
        ans += plus*3
        r -= check
        c -= check
        #print('행보',3)
    n -= 1
    check = 2**(n-1)
    plus = 4**(n-1)
print(ans)