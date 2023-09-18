import sys
input = sys.stdin.readline


def trap_stepping(y:int, x:int) -> tuple[int, int]:
    # 파라미터로 위치 준 이유는
    # 함정 위에서 커맨드 방향으로 움직일 수 없는 경우를 위해
    global curHp, dead_trap

    if clip["DX"]:
        damage = 1
    else:
        damage = 5

    if board[y][x] == "^":
        curHp -= damage
    
    if curHp <= 0:
        if reincarnation():
            # 부활
            return st_pos
        else:
            dead_trap = True

    return y,x

def item_stepping(y:int, x:int) -> None:
    global weapon, armor, clip_cnt, clip, board

    bT, bS = items[(y,x)]
    if bT == "W":
        weapon = bS
    elif bT == "A":
        armor = bS
    else:
        if clip_cnt <= 3 and not clip[bS]:
            clip_cnt += 1
            clip[bS] = True
    board[y][x] = "."


def reincarnation() -> bool:
    global clip, clip_cnt, curHp

    if clip["RE"]:
        # 사용 후 소멸
        clip["RE"] = False
        clip_cnt -= 1
        curHp = maxHp
        return True
    
    return False

def level_up(mExp:int) -> None:
    global exp, level, maxHp, curHp, atk, dfn

    if clip["EX"]:
        exp += int(mExp*1.2)
    else:
        exp += mExp

    # 레벨 업 
    if exp >= level*5:
        level += 1
        exp = 0
        maxHp += 5
        curHp = maxHp
        atk += 2
        dfn += 2


def boss_stepping(y:int, x:int) -> tuple[int, int]:
    global curHp, dead_monster, board, alive_boss
    name = get_name[(y,x)]
    # monster[name] = [mAtk, mDfn, mHp, mExp]
    mAtk, mDfn, mHp, mExp = monster[name]

    # 보스 몬스터 첫 공격을 안받음
    # 순서가 그러면
    """
    나 일빠따 때림
    나 이빠따 때림
    몬 일빠따 때림
    """
    idx = 0

    if clip["HU"]:
        curHp = maxHp
        my_atk = get_atk(idx==0)
        mHp -= max(1, my_atk-mDfn)
        idx += 1


    while True:

        my_atk = get_atk(idx==0)

        mHp -= max(1, my_atk-mDfn)
        if mHp <= 0: # 보스 뒤짐
            board[y][x] = "@"

            if clip["HR"]:
                curHp = min(maxHp, curHp+3)
            level_up(mExp)
            # 보스 죽임
            alive_boss = False

            # 이제 이자리는 내꺼임 ㅅㄱ
            return y,x

        curHp -= max(1, mAtk-(dfn+armor))
        if curHp <= 0: # 주인공 뒤짐

            # 개같이 부활
            if reincarnation():
                return st_pos
            else:
                # 사망시엔 주인공 위치 출력하면 안됨
                dead_monster = name
                return y,x

        idx += 1


def monster_stepping(y:int, x:int) -> tuple[int,int]:
    global curHp, dead_monster, board
    name = get_name[(y,x)]
    # monster[name] = [mAtk, mDfn, mHp, mExp]
    mAtk, mDfn, mHp, mExp = monster[name]

    idx = 0

    while True:
        # 첫턴은 템빨이 있음
        my_atk = get_atk(idx==0)

        mHp -= max(1, my_atk-mDfn)
        if mHp <= 0: # 몬스터 뒤짐
            board[y][x] = "."

            if clip["HR"]:
                curHp = min(maxHp, curHp+3)

            level_up(mExp)

            # 이제 이자리는 내꺼임 ㅅㄱ
            return y,x

        curHp -= max(1, mAtk-(dfn+armor))
        if curHp <= 0: # 주인공 뒤짐

            # 개같이 부활
            if reincarnation():
                return st_pos
            else:
                # 사망시엔 주인공 위치 출력하면 안됨
                dead_monster = name
                return y,x

        idx += 1


def get_atk(first:bool) -> int:

    if not first:
        return atk+weapon
    
    if clip["CO"] and clip["DX"]:
        return (atk+weapon)*3
    elif clip["CO"]:
        return (atk+weapon)*2
    return atk+weapon



d = {"L":(0,-1), "R":(0,1), "U":(-1,0), "D":(1,0)}

maxHp = 20
curHp,atk,dfn = 20, 2, 2
exp = 0
level = 1

dead_monster = ""
dead_trap = False
alive_boss = True


n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

cmd = list(input().rstrip())
# 몬스터의 갯수
mon_cnt = 0 
# 장신구의 갯수
item_cnt = 0 

# 주인공 위치
y,x = -1,-1
monster = dict()
get_name = dict()

items = dict()
item_list = ["HR", "RE", "CO", "EX", "DX", "HU", "CU"]
clip = {item:False for item in item_list}
clip_cnt = 0

weapon, armor = 0,0

turn = 0
press_key = True


for i in range(n):
    for j in range(m):
        if board[i][j] == "@":
            board[i][j] = "."
            st_pos = (i,j)
            y,x = i,j
        elif board[i][j] == "&":
            mon_cnt += 1
        elif board[i][j] == "M":
            mon_cnt += 1
            boss_pos = (i,j)
        elif board[i][j] == "B":
            item_cnt += 1


for _ in range(mon_cnt):
    mR,mC,name,mAtk,mDfn,mHp,mExp = input().rstrip().split()
    mR,mC,mAtk,mDfn,mHp,mExp = int(mR)-1,int(mC)-1,int(mAtk),int(mDfn),int(mHp),int(mExp)
    get_name[(mR,mC)] = name
    # 순서 중요
    monster[name] = [mAtk, mDfn, mHp, mExp]

# print(monster)

for _ in range(item_cnt):
    bR,bC,bT,bS = input().rstrip().split()
    bR,bC = int(bR)-1, int(bC)-1

    if bT=="O":
        items[(bR,bC)] = (bT,bS)
    else:
        # W 공격력
        # A 방어력
        bS = int(bS)
        items[(bR,bC)] = (bT,bS)

for i in range(len(cmd)):
    dy,dx = d[cmd[i]]
    ny,nx = y+dy,x+dx

    if ny < 0 or nx < 0 or ny >= n or nx >= m:
        # 이전 위치가 함정인지 체크 후 체력깎음
        y,x = trap_stepping(y,x)
    elif board[ny][nx] == ".":
        y,x = ny,nx
    elif board[ny][nx] == "#":
        # 역시 이전 위치가 함정인지
        y,x = trap_stepping(y,x)
    elif board[ny][nx] == "^":
        y,x = trap_stepping(ny,nx)
    elif board[ny][nx] == "B":
        y,x = ny,nx
        item_stepping(y,x)
    elif board[ny][nx] == "&":
        y,x = monster_stepping(ny,nx)
    elif board[ny][nx] == "M":
        y,x = boss_stepping(ny,nx)

    turn += 1

    if not alive_boss or dead_monster or dead_trap:
        press_key = False
        break

if press_key:
    board[y][x] = "@"

for i in range(n):
    print(*board[i],sep='')

print(f"Passed Turns : {turn}")
print(f"LV : {level}")
print(f"HP : {max(0,curHp)}/{maxHp}")
print(f"ATT : {atk}+{weapon}")
print(f"DEF : {dfn}+{armor}")
print(f"EXP : {exp}/{level*5}")

if not alive_boss:
    print("YOU WIN!")
elif dead_monster:
    print(f"YOU HAVE BEEN KILLED BY {dead_monster}..")
elif dead_trap:
    print(f"YOU HAVE BEEN KILLED BY SPIKE TRAP..")
else:
    print("Press any key to continue.")


# 반례는 범위 밖 continue 