import sys
input = sys.stdin.readline

dx = [0,1,-1,0,1,1,-1,-1]
dy = [1,0,0,-1,1,-1,1,-1]

def sprint_summber_winter():
    for y in range(n):
        for x in range(n):
            if trees[y][x]: # 이자리에 나무 한그루 이상 있다면
                death = 0
                new = dict()
                # 이부분을 age 정렬한다음에 넘어간다면 break 걸고 연산하는게 빠를까?

                for age, cnt in sorted(trees[y][x].items()):
                    if now[y][x] >= age*cnt:
                        now[y][x] -= age*cnt
                        new[age+1] = cnt
                    else:
                        tmp = now[y][x] // age
                        death += age // 2 * (cnt - tmp)

                        if not tmp:
                            continue

                        now[y][x] -= age*tmp
                        new[age+1] = tmp

                now[y][x] += death # 여름 행위
                trees[y][x] = new # 새로 나이 먹은 것들

            now[y][x] += foods[y][x] # 겨울 행위

def fall():
    for y in range(n):
        for x in range(n):
            new = 0
            for age, cnt in trees[y][x].items():
                if age%5 == 0:
                    new += cnt
            
            if new:
                for i in range(8):
                    nx = dx[i] + x
                    ny = dy[i] + y

                    if 0 > nx or 0 > ny or nx >= n or ny >= n:
                        continue
                    if 1 not in trees[ny][nx]:
                        trees[ny][nx][1] = 0
                    trees[ny][nx][1] += new

n,m,k = map(int,input().split())
now = [[5]*n for _ in range(n)]
trees = [[{} for _ in range(n)] for _ in range(n)] # dict에 key:age, value:cnt
foods = [list(map(int,input().split())) for _ in range(n)]

for _ in range(m):
    y,x,z = map(int,input().split())
    trees[y-1][x-1][z] = 1 # trees[y][x] 에 z살짜리가 한그루

for year in range(k):
    sprint_summber_winter()
    fall()

ans = 0

for y in range(n):
    for x in range(n):
        ans += sum(trees[y][x].values())

print(ans)