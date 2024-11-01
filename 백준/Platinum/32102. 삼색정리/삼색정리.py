import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def solve(n:int, m:int, r:int, g:int, b:int) -> str:
    
    res = [[''] * m for _ in range(n)]
    color = [[r, 'R'], [g, 'G'], [b, 'B']]
    color.sort()

    half = (n * m + 1) // 2
    if color[-1][0] > half:
        print("NO")
        return

    if n >= m:
        for i in range(n):
            for j in range(m):
                if (i+j)%2: continue
                res[i][j] = color[-1][1]
                color[-1][0] -= 1

                if not color[-1][0]:
                    color.pop()

                    if len(color) == 2:
                        color.reverse()

        for i in range(n):
            for j in range(m):
                if not(i+j)%2: continue
                res[i][j] = color[-1][1]
                color[-1][0] -= 1

                if not color[-1][0]:
                    color.pop()

                    if len(color) == 2:
                        color.reverse()
    else:
        for i in range(m):
            for j in range(n):
                if not(i+j)%2: continue
                res[j][i] = color[-1][1]
                color[-1][0] -= 1

                if not color[-1][0]:
                    color.pop()

                    if len(color) == 2:
                        color.reverse()
        for i in range(m):
            for j in range(n):
                if (i+j)%2: continue
                res[j][i] = color[-1][1]
                color[-1][0] -= 1

                if not color[-1][0]:
                    color.pop()

                    if len(color) == 2:
                        color.reverse()

    return res


n,m = map(int,input().split())
r,g,b = map(int,input().split())

res = solve(n, m, r, g, b)
if res:
    print("YES")
    for ans in res:
        print(*ans,sep='')