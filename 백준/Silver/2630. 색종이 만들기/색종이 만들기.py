import sys
input = sys.stdin.readline

N = int(input().rstrip())
paper = [list(map(int, input().rstrip().split())) for _ in range(N)] 

result = []

def find(x, y, N) :
    color = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] :
                find(x, y, N//2)
                find(x, y+N//2, N//2)
                find(x+N//2, y, N//2)
                find(x+N//2, y+N//2, N//2)
                return
    if color == 0 : result.append(0)
    else : result.append(1)


find(0,0,N)
print(result.count(0))
print(result.count(1))