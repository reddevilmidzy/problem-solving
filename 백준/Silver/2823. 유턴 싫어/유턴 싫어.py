import sys
input=sys.stdin.readline
r,c=map(int,input().split())
graph=[list(map(str,input().rstrip())) for _ in range(r)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]

for i in range(r):
    for j in range(c):
        if graph[i][j]=='.':
            road=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0 > nx or 0 > ny or nx >= r or ny >= c:
                    continue
                if graph[nx][ny]=='.':
                    road+=1
            if road >= 2:
                pass
            else:
                print(1)
                exit()
print(0)