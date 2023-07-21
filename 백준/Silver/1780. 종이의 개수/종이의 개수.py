import sys
input = sys.stdin.readline
t = int(input())
graph = [list(map(int,input().rstrip().split())) for _ in range(t)]
ans = [0,0,0]

def solution(x,y,n):
    global ans

    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        solution(x+k*n//3, y+l*n//3, n//3)
                return
    ans[check] += 1

solution(0,0,t)
print(ans[-1],ans[0],ans[1],sep='\n')