import sys
input = sys.stdin.readline

def act_gold_key():
    global key_idx, s, win, cur, social, city, island, bought

    if gold_keys[key_idx][0] == 1:
        s += gold_keys[key_idx][1]
    
    # 은행에 주기
    elif gold_keys[key_idx][0] == 2:
        if s >= gold_keys[key_idx][1]:
            s -= gold_keys[key_idx][1]
        else: # 돈 지불 못함
            win = False
    elif gold_keys[key_idx][0] == 3:
        if s >= gold_keys[key_idx][1]:
            s -= gold_keys[key_idx][1]
            social += gold_keys[key_idx][1]
        else: # 돈 지불 못함
            win = False
    else:
        cur += gold_keys[key_idx][1]
        cur %= n*4-4
        if cur - gold_keys[key_idx][1] < 0:
            s += w
        
        if type(board[cur]) == int:
            if board[cur] <= s and not bought[cur]:
                bought[cur] = True
                s -= board[cur]
                city -= 1
        elif board[cur] == "사회복지기금":
            s += social
            social = 0
        elif board[cur] == "우주여행":
            # 시작칸으로 이동
            cur = 0
            s += w
        elif board[cur] == "무인도":
            island = 3

    key_idx += 1
    key_idx %= g

# 보드크기, 시작 돈, 월급, 황금열쇠 갯수
n,s,w,g = map(int,input().split())

gold_keys = [list(map(int,input().split())) for _ in range(g)]
key_idx = 0
# 도시 개수
city = 0
cur = 0
bought = dict()
win = True
social = 0
island = 0

"""
1 x: x받기
2 x: x내기
3 x: 사회복지 기금 x원 기부
4 x: 앞으로 이동
"""

board = [""]*(4*n-4)
board[0] = "시작"
board[n-1] = "무인도"
board[2*n-2] = "사회복지기금"
board[3*n-3] = "우주여행"

idx = 1

while idx<4*n-4:
    tmp = input().rstrip().split()
    if tmp[0] == "G":
        board[idx] = "G"
    else:
        city += 1
        bought[idx] = False
        board[idx] = int(int(tmp[1]))
    
    idx += 1
    if idx in {n-1, 2*n-2, 3*n-3}:
        idx += 1

cnt = int(input())
for _ in range(cnt):
    one,two = map(int,input().split())
    if island > 0:
        island -= 1
        if one == two: # 탈출
            island = 0
        continue

    cur += (one+two)

    if cur >= n*4-4:
        s += w*(cur//(n*4-4))

    cur %= n*4-4


    if type(board[cur]) == int:
        if board[cur] <= s and not bought[cur]:
            bought[cur] = True
            s -= board[cur]
            city -= 1

    # 황금열쇠
    elif board[cur] == "G":
        act_gold_key()
        if not win:
            print("LOSE")
            break
    elif board[cur] == "사회복지기금":
        s += social
        social = 0
    elif board[cur] == "우주여행":
        # 시작칸으로 이동
        cur = 0
        s += w

    elif board[cur] == "무인도":
        island = 3

else:
    if city:
        print("LOSE")
    else:
        print("WIN")

