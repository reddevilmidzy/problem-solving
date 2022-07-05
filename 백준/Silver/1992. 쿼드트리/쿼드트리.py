import sys
input = sys.stdin.readline

n = int(input())
video = [list(map(int,input().rstrip())) for _ in range(n)]

def solution(x,y,n):
    check = video[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != video[i][j]:
                print('(',end='')
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                print(')',end='')
                return
    print(0,end='') if check == 0 else print(1,end='')
    return
solution(0,0,n)