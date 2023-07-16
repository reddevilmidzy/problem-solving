import sys
input = sys.stdin.readline
INF = int(1e9)
dy = (1,-1,0,0)
dx = (0,0,1,-1)

def move(y:int, x:int, d:int) -> int:
    res = 0
    visited = [[[False]*m for _ in range(n)] for _ in range(4)]
    
    while 0<=y<n and 0<=x<m and board[y][x] != "C":
        if visited[d][y][x]:
            return INF
        visited[d][y][x] = True
        if board[y][x] == "/":
            if d==0: d=3
            elif d==1: d=2
            elif d==2: d=1
            else: d=0
        elif board[y][x] == "\\":
            d = (d+2)%4
        y,x = dy[d]+y, dx[d]+x
        res += 1
    return res

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

y,x = map(int,input().split())
ans = []

way = {0:"D", 1:"U", 2:"R", 3:"L"}
order = [2,0,1,3]
for i in range(4):
    ans.append((move(y-1,x-1,i), -order[i], way[i]))
ans.sort(reverse=True)
dist,tmp,w = ans[0]
if dist==INF:print(w,"Voyager",sep='\n')
else:print(w,dist,sep='\n')