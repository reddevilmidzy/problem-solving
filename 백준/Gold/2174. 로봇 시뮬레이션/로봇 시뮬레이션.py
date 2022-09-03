import sys
input = sys.stdin.readline

a,b = map(int,input().split()) # 좌표 정보
n,m = map(int,input().split()) # 로봇갯수, 명령어갯수
graph = [[0]*(a+1) for _ in range(b+1)]
robot = dict()
move = {'N':[1,0], 'W':[0,-1], 'S':[-1,0],'E':[0,1]}
tmp = ['N','W','S','E']
res = ''
for i in range(1,n+1):
    x,y,c = map(str,input().rstrip().split())
    x,y = int(x),int(y)
    graph[y][x] = i
    robot[i] = [y,x,c]

#print(robot)

for i in range(m):
    ro,code,move_cnt = map(str,input().rstrip().split())
    ro = int(ro)
    nx = robot[ro][1]
    ny = robot[ro][0]
    pos = robot[ro][2]
    move_cnt = int(move_cnt)
    # now = 0
    #print('x',x, 'y',y)
    if code == 'L':
        move_cnt %= 4
        now = (tmp.index(pos)+move_cnt)%4
        robot[ro][2] = tmp[now]
        #print('방향',robot[ro][2])
    elif code=='R':
        move_cnt %= 4
        #print('테스트케이스')
        #print(tmp.index(pos), move_cnt, (-3)%4)
        now = (tmp.index(pos)-move_cnt)%4
        robot[ro][2] = tmp[now]
        #print('방향',robot[ro][2])
        #pass
    else:
        for j in range(move_cnt):
            nx = nx + move[pos][1]
            ny = ny + move[pos][0]
            #print(nx,ny)
            #print('nx',nx,'ny',ny)
            if 1 > nx or nx > a or 1 > ny or ny > b:
                #print('인덱스 벗어남')
                if res == '':
                    res = f'Robot {ro} crashes into the wall'
                    #print(ro)
                break
            if graph[ny][nx] != 0:
                if res =='':
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

print(res if res!='' else 'OK')
