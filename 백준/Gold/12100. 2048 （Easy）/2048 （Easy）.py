from itertools import product
import sys
input = sys.stdin.readline

def north(n:int, board: list[list[int]]):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        tmp = []
        tmp_board = [board[j][i] for j in range(n)]
        while 0 in tmp_board:
            tmp_board.remove(0)
        m = len(tmp_board)
        j = 0
        while j < m - 1:
            if tmp_board[j] == tmp_board[j+1]:
                tmp.append(tmp_board[j]*2)
                j += 2
                if j == m-1:
                    tmp.append(tmp_board[j])
            elif tmp_board[j] != tmp_board[j+1]:
                tmp.append(tmp_board[j])
                j += 1
                if j == m-1:
                    tmp.append(tmp_board[j])
        if m == 1:
            tmp.append(tmp_board[0])

        tmp.extend([0]*(n-len(tmp)))
        for k in range(n):
            res[k][i] = tmp[k]

    return res

def south(n: int, board: list[list[int]]):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        tmp = []
        tmp_board = [board[j][i] for j in range(n)]
        while 0 in tmp_board:
            tmp_board.remove(0)
        m = len(tmp_board)
        j = m - 1
        while j > 0:
            if tmp_board[j] == tmp_board[j-1]:
                tmp.append(tmp_board[j]*2)
                j -= 2
                if j == 0:
                    tmp.append(tmp_board[j])
            elif tmp_board[j] != tmp_board[j-1]:
                tmp.append(tmp_board[j])
                j -= 1
                if j == 0:
                    tmp.append(tmp_board[j])
        if m == 1:
            tmp.append(tmp_board[0])
        tmp.extend([0]*(n-len(tmp)))
        for k in range(n):
            res[n - k - 1][i] = tmp[k]

    return res

def east(n:int, board: list[list[int]]):
    res = []
    for i in range(n):
        tmp = []
        tmp_board = [board[i][j] for j in range(n)]
        while 0 in tmp_board:
            tmp_board.remove(0)
        m = len(tmp_board)
        j = m-1
        while j > 0:
            if tmp_board[j] == tmp_board[j-1]:
                tmp.append(tmp_board[j]*2)
                j -= 2
                if j == 0:
                    tmp.append(tmp_board[j])
            elif tmp_board[j] != tmp_board[j-1]:
                tmp.append(tmp_board[j])
                j -= 1
                if j == 0:
                    tmp.append(tmp_board[j])

        if m == 1:
            tmp.append(tmp_board[0])
        tmp.extend([0]*(n-len(tmp)))
        res.append(tmp[::-1])
    return res

def west(n, board: list[list[int]]):
    res = []
    for i in range(n):
        tmp = []
        tmp_board = [board[i][j] for j in range(n)]
        while 0 in tmp_board: # 시간 많이 안걸리려나
            tmp_board.remove(0)
        j = 0
        m = len(tmp_board)

        while j < m-1:
            if tmp_board[j] == tmp_board[j+1]:
                tmp.append(tmp_board[j]*2)
                j += 2
                if j == m-1:
                    tmp.append(tmp_board[j])
            elif tmp_board[j] != tmp_board[j+1]:
                tmp.append(tmp_board[j])
                j += 1
                if j == m-1:
                    tmp.append(tmp_board[j])
        
        if m == 1:
            tmp.append(tmp_board[0])

        tmp.extend([0]*(n-len(tmp)))
        res.append(tmp[::])

    return res
move = [east, west, south, north]
way = [i for i in range(4)] # 동서남북 
n = int(input()) # 1이라면 안변함
board = [list(map(int,input().split())) for _ in range(n)]

def max_block(board: list[list[int]]):
    res = 0
    for i in range(n):
        for j in range(n):
            res = max(res, board[i][j])
    return res
ans = max_block(board)
for x in product(way, repeat=5):
    tmp_ = board[::]
    for y in x:
        tmp_ = move[y](n, tmp_)
    ans = max(ans, max_block(tmp_))
print(ans)    