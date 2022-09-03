import sys
input = sys.stdin.readline

a,b = map(int,input().split()) # 좌표 정보
n,m = map(int,input().split()) # 로봇갯수, 명령어갯수
graph = [[0]*(a+1) for _ in range(b+1)] # 그래프
robot = dict() # 로봇의 위치 그리고 방향 담을 dict
move = {'N':[1,0], 'W':[0,-1], 'S':[-1,0],'E':[0,1]}
tmp = ['N','W','S','E']
res = 'OK'
for i in range(1,n+1):
    x,y,c = map(str,input().rstrip().split())
    x,y = int(x),int(y)
    graph[y][x] = i
    robot[i] = [y,x,c]

for i in range(m):
    ro,code,move_cnt = map(str,input().rstrip().split())
    ro = int(ro)
    nx = robot[ro][1]
    ny = robot[ro][0]
    pos = robot[ro][2]
    move_cnt = int(move_cnt)

    if code == 'L':
        move_cnt %= 4
        now = (tmp.index(pos)+move_cnt)%4
        robot[ro][2] = tmp[now]

    elif code=='R':
        move_cnt %= 4
        now = (tmp.index(pos)-move_cnt)%4
        robot[ro][2] = tmp[now]
    else:
        for j in range(move_cnt):
            nx = nx + move[pos][1]
            ny = ny + move[pos][0]
            # 인덱스 벗어난다면
            if 1 > nx or nx > a or 1 > ny or ny > b:
                if res == 'OK':
                    res = f'Robot {ro} crashes into the wall'
                break
            # 이동한 자리에 이미 다른 로봇이 있다면
            if graph[ny][nx] != 0:
                if res == 'OK':
                    res = f'Robot {ro} crashes into robot {graph[ny][nx]}'
                break
        else:
            # 변경한 위치 로봇 적음
            graph[ny][nx] = ro
            # 이전에 있던 위치 지움
            graph[robot[ro][0]][robot[ro][1]] = 0
        
            # dict 도 변경
            robot[ro][0] = ny
            robot[ro][1] = nx

print(res)