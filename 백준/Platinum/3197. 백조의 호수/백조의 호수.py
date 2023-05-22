import sys
input = sys.stdin.readline

d = [(1,0), (0,1), (-1,0), (0,-1)]
def out_of_range(ny:int, nx:int) -> bool:
    return ny < 0 or nx < 0 or ny >= r or nx >= c

def find(ancestor: list[int], cur: int) -> int:
    if ancestor[cur] == cur: return cur
    par = find(ancestor, ancestor[cur])
    ancestor[cur] = par
    return par

r,c = map(int,input().split())
board = [list(input().rstrip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
parent = [[-1]*c for _ in range(r)]
swan = []
melted = []

for y in range(r):
    for x in range(c):
        if board[y][x] == "L":
            swan.append(y)
            swan.append(x)
            board[y][x] = "."
            melted.append((y,x))
            visited[y][x] = True
        elif board[y][x] == ".":
            visited[y][x] = True
            melted.append((y,x))

sw_y, sw_x, sw_r, sw_c = swan

idx = 1
# 처음에 녹아있는 부분
# 서로 연결해줌

for y, x in melted:
    if parent[y][x] != -1: continue
    stk = [(y,x)]
    while stk:
        y,x = stk.pop()
        parent[y][x] = idx
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            #  범위밖, 이미 다른 자식, 얼음 이라면 
            if out_of_range(ny,nx): continue
            if parent[ny][nx] != -1: continue
            if board[ny][nx] == "X": continue
            stk.append((ny,nx))
    idx += 1

ancestor = [i for i in range(idx)]

ans = 0
will_melted = []

while melted:
    y,x = melted.pop()
    if board[y][x] == "X":
        board[y][x] = "."
        types = set()
        anc_types = set()
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if out_of_range(ny,nx): continue
            if board[ny][nx] != "X":
                types.add(parent[ny][nx])
                anc_types.add(find(ancestor, parent[ny][nx]))
        min_anc = min(anc_types)
        parent[y][x] = min_anc
        for t in types:
            # union 느낌
            ac = find(ancestor, t)
            ancestor[ac] = min_anc
    for dy,dx in d:
        ny,nx = y+dy,x+dx
        if out_of_range(ny,nx): continue
        if not visited[ny][nx]:
            will_melted.append((ny,nx))
            visited[ny][nx] = True
    if not melted:
        if find(ancestor, parent[sw_y][sw_x]) == find(ancestor, parent[sw_r][sw_c]):
            print(ans)
            break
        ans += 1
        melted = will_melted[::]
        will_melted.clear()