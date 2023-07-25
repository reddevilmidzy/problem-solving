from sys import stdin
input = stdin.readline

n = 3

def turn_foreward(arr:list[list[int]], is_clock:bool) -> None:
    if is_clock:
            arr[0][0],arr[0][1],arr[0][2],arr[1][0],arr[1][1],arr[1][2],arr[2][0],arr[2][1],arr[2][2]=\
                arr[2][0],arr[1][0],arr[0][0],arr[2][1],arr[1][1],arr[0][1],arr[2][2],arr[1][2],arr[0][2]
    else:
        arr[0][0],arr[1][0],arr[2][0],arr[0][1],arr[1][1],arr[2][1],arr[0][2],arr[1][2],arr[2][2]=\
            arr[0][2],arr[0][1],arr[0][0],arr[1][2],arr[1][1],arr[1][0],arr[2][2],arr[2][1],arr[2][0]

def move(way:int, turn:int):
    global u,l,f,r,b,d
    if way == 1:
        turn_foreward(f, turn > 0)
        if turn > 0:
            u[2][0],u[2][1],u[2][2],r[0][0],r[1][0],r[2][0],d[0][2],d[0][1],d[0][0],l[2][2],l[1][2],l[0][2] = l[2][2],l[1][2],l[0][2],u[2][0],u[2][1],u[2][2],r[0][0],r[1][0],r[2][0],d[0][2],d[0][1],d[0][0]
        else:
            u[2][0],u[2][1],u[2][2],r[0][0],r[1][0],r[2][0],d[0][2],d[0][1],d[0][0],l[2][2],l[1][2],l[0][2] = r[0][0],r[1][0],r[2][0],d[0][2],d[0][1],d[0][0],l[2][2],l[1][2],l[0][2],u[2][0],u[2][1],u[2][2]
    elif way == 4:
        turn_foreward(u, turn > 0)
        if turn > 0:
            l[0][0],l[0][1],l[0][2],f[0][0],f[0][1],f[0][2],r[0][0],r[0][1],r[0][2],b[0][0],b[0][1],b[0][2] = f[0][0],f[0][1],f[0][2],r[0][0],r[0][1],r[0][2],b[0][0],b[0][1],b[0][2],l[0][0],l[0][1],l[0][2]
        else:
            l[0][0],l[0][1],l[0][2],f[0][0],f[0][1],f[0][2],r[0][0],r[0][1],r[0][2],b[0][0],b[0][1],b[0][2] = b[0][0],b[0][1],b[0][2],l[0][0],l[0][1],l[0][2],f[0][0],f[0][1],f[0][2],r[0][0],r[0][1],r[0][2]
    elif way == 0:
        turn_foreward(l, turn > 0)
        if turn > 0:
            u[0][0],u[1][0],u[2][0],f[0][0],f[1][0],f[2][0],d[0][0],d[1][0],d[2][0],b[2][2],b[1][2],b[0][2] = b[2][2],b[1][2],b[0][2],u[0][0],u[1][0],u[2][0],f[0][0],f[1][0],f[2][0],d[0][0],d[1][0],d[2][0]
        else:
            u[0][0],u[1][0],u[2][0],f[0][0],f[1][0],f[2][0],d[0][0],d[1][0],d[2][0],b[2][2],b[1][2],b[0][2] = f[0][0],f[1][0],f[2][0],d[0][0],d[1][0],d[2][0],b[2][2],b[1][2],b[0][2],u[0][0],u[1][0],u[2][0]
    elif way == 2:
        turn_foreward(r, turn > 0)
        if turn > 0:
            d[2][2],d[1][2],d[0][2],f[2][2],f[1][2],f[0][2],u[2][2],u[1][2],u[0][2],b[0][0],b[1][0],b[2][0] = b[0][0],b[1][0],b[2][0],d[2][2],d[1][2],d[0][2],f[2][2],f[1][2],f[0][2],u[2][2],u[1][2],u[0][2]
        else:
            d[2][2],d[1][2],d[0][2],f[2][2],f[1][2],f[0][2],u[2][2],u[1][2],u[0][2],b[0][0],b[1][0],b[2][0] = f[2][2],f[1][2],f[0][2],u[2][2],u[1][2],u[0][2],b[0][0],b[1][0],b[2][0],d[2][2],d[1][2],d[0][2]
    elif way == 5:
        turn_foreward(d, turn > 0)
        if turn > 0:
            l[2][0],l[2][1],l[2][2],f[2][0],f[2][1],f[2][2],r[2][0],r[2][1],r[2][2],b[2][0],b[2][1],b[2][2] = b[2][0],b[2][1],b[2][2],l[2][0],l[2][1],l[2][2],f[2][0],f[2][1],f[2][2],r[2][0],r[2][1],r[2][2]
        else:
            l[2][0],l[2][1],l[2][2],f[2][0],f[2][1],f[2][2],r[2][0],r[2][1],r[2][2],b[2][0],b[2][1],b[2][2] = f[2][0],f[2][1],f[2][2],r[2][0],r[2][1],r[2][2],b[2][0],b[2][1],b[2][2],l[2][0],l[2][1],l[2][2]
    elif way == 3:
        turn_foreward(b, turn > 0)
        if turn > 0:
            d[2][0],d[2][1],d[2][2],r[2][2],r[1][2],r[0][2],u[0][2],u[0][1],u[0][0],l[0][0],l[1][0],l[2][0] = l[0][0],l[1][0],l[2][0],d[2][0],d[2][1],d[2][2],r[2][2],r[1][2],r[0][2],u[0][2],u[0][1],u[0][0]
        else:
            d[2][0],d[2][1],d[2][2],r[2][2],r[1][2],r[0][2],u[0][2],u[0][1],u[0][0],l[0][0],l[1][0],l[2][0] = r[2][2],r[1][2],r[0][2],u[0][2],u[0][1],u[0][0],l[0][0],l[1][0],l[2][0],d[2][0],d[2][1],d[2][2]

def pr(idx:int):
    print(f"Scenario #{idx}:")
    print("      ", end='')
    print("\n      ".join(" ".join(i) for i in u))

    for i in range(n):
        print(*l[i], *f[i], *r[i], *b[i], sep=' ',)

    print("      ", end='')
    print("\n      ".join(" ".join(i) for i in d))

    if idx != t:
        print()

t = int(input())
for idx in range(1, t+1):
    u = [list(input().lstrip().rstrip().split()) for _ in range(n)]
    body = [list(input().lstrip().rstrip().split()) for _ in range(n)]
    d = [list(input().lstrip().rstrip().split()) for _ in range(n)]

    l = [[body[i][j] for j in range(n)] for i in range(n)]
    f = [[body[i][j] for j in range(n, n+3)] for i in range(n)]
    r = [[body[i][j] for j in range(2*n, 2*n+3)] for i in range(n)]
    b = [[body[i][j] for j in range(3*n, 3*n+3)] for i in range(n)]

    cnt = int(input())
    for _ in range(cnt):
        way,turn = map(int,input().split())
        move(way,turn)
    pr(idx)