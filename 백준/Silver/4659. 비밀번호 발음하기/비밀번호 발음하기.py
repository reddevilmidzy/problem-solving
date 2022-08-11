import sys
input = sys.stdin.readline

mom = ['a','e','i','o','u']

while True:
    pw = list(input().rstrip())
    ans = True
    inmom = False
    cntmom = 0
    cntson = 0
    if pw == ['e','n','d']:
        break
    for i in range(len(pw)):
        if pw[i] in mom:
            inmom = True
            cntmom += 1
            if cntmom == 3:
                ans = False
                break
            cntson = 0
        else:
            cntson += 1
            if cntson == 3:
                ans = False
                break
            cntmom = 0
        if (pw[i] != 'e' and pw[i] != 'o') and i < len(pw)-1 and pw[i] == pw[i+1]:
            ans = False
            break
    if not inmom:
        ans = False
    if ans:
        print(f'<{"".join(pw)}> is acceptable.')
    else:
        print(f'<{"".join(pw)}> is not acceptable.')