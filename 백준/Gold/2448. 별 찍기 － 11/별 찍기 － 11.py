import sys
input = sys.stdin.readline
N = int(input())

arr = [[' ']*(2*N-1) for i in range(N)]

def makeStar(n, x, y):
    
    if n == 3:
        arr[y][x] = '*'
        arr[y+1][x-1:x+2] = '* *'
        arr[y+2][x-2:x+3] = '*****'
        return
    else:
        makeStar(n / 2, x, y)
        makeStar(n / 2, int(x - (n / 2)), int(y + (n / 2)))
        makeStar(n / 2, int(x + (n / 2)), int(y + (n / 2)))

makeStar(N, N-1, 0)

for i in arr:
    print(''.join(i))