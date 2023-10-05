n,l = map(int,input().split())

tot = (l)*(l+1)//2

while True:
    if l%2:
        if not n%l:
            cen = n//l
            break
    else:
        if not n%(l//2) and (n//(l//2)%2):
            cen = n//(l//2)//2
            break
    tot += l
    l += 1
    if tot>n or l>100:
        print(-1)
        exit()


if l%2 and cen-(l//2) >= 0:
    print(*range(cen-(l//2), cen+(l//2)+1))
elif not l%2 and cen-((l//2)-1) >= 0:
    print(*range(cen-((l//2)-1), cen+(l//2)+1))
else:
    print(-1)