def bt(s:list[int], idx:int) -> None:
    if idx > n:
        for x,y in cnf:
            if x < 0:
                x = not s[abs(x)]
            else:
                x = s[abs(x)]
            if y < 0:
                y = not s[abs(y)]
            else:
                y = s[abs(y)]

            if not (x | y):
                break
        else:
            print(1)
            exit()

        return
    for i in [False, True]:
        s[idx] = i
        bt(s, idx+1)
        s[idx] = not i

n,m = map(int,input().split())
cnf = [list(map(int,input().split())) for _ in range(m)]
bt([False]*(n+1), 1)
print(0)