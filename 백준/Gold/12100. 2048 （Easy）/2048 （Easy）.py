from sys import stdin
input = stdin.readline

def solve(move:int, board: list[list[int]]) -> list[list[int]]:
    if move == 0:
        res = []
        for i in range(n):
            tmp = [0]*n
            idx = 0
            tmp_board = [board[i][j] for j in range(n) if board[i][j]]
            m = len(tmp_board)
            j = m-1
            while j > 0:
                if tmp_board[j] == tmp_board[j-1]:
                    tmp[idx] = tmp_board[j]*2
                    idx += 1
                    j -= 2
                    if j == 0:
                        tmp[idx] = tmp_board[j]
                        idx += 1
                else:
                    tmp[idx] = tmp_board[j]
                    idx += 1
                    j -= 1
                    if j == 0:
                        tmp[idx] = tmp_board[j]
                        idx += 1
            if m == 1:
                tmp[idx] = tmp_board[0]

            res.append(tmp[::-1])

    elif move == 1:
        res = []
        for i in range(n):
            tmp = [0]*n
            idx = 0
            tmp_board = [board[i][j] for j in range(n) if board[i][j]]
            j = 0
            m = len(tmp_board)

            while j < m-1:
                if tmp_board[j] == tmp_board[j+1]:
                    tmp[idx] = tmp_board[j]*2
                    idx += 1
                    j += 2
                    if j == m-1:
                        tmp[idx] = tmp_board[j]
                        idx += 1
                else:
                    tmp[idx] = tmp_board[j]
                    idx += 1
                    j += 1
                    if j == m-1:
                        tmp[idx] = tmp_board[j]
                        idx +=  1
            
            if m == 1:
                tmp[idx] = tmp_board[0]

            res.append(tmp[:])

    elif move == 2:
        res = [[0]*n for _ in range(n)]
        for i in range(n):
            tmp = [0]*n
            idx = 0
            tmp_board = [board[j][i] for j in range(n) if board[j][i]]
            m = len(tmp_board)
            j = m - 1
            while j > 0:
                if tmp_board[j] == tmp_board[j-1]:
                    tmp[idx] = tmp_board[j]*2
                    idx += 1
                    j -= 2
                    if j == 0:
                        tmp[idx] = tmp_board[j]
                        idx += 1
                else:
                    tmp[idx] = tmp_board[j]
                    idx += 1
                    j -= 1
                    if j == 0:
                        tmp[idx] = tmp_board[j]
                        idx += 1
            if m == 1:
                tmp[idx] = tmp_board[0]

            for k in range(n):
                res[n - k - 1][i] = tmp[k]
    else:
        res = [[0]*n for _ in range(n)]
        for i in range(n):
            tmp = [0]*n
            idx = 0
            tmp_board = [board[j][i] for j in range(n) if board[j][i]]
            m = len(tmp_board)
            j = 0
            while j < m - 1:
                if tmp_board[j] == tmp_board[j+1]:
                    tmp[idx] = tmp_board[j]*2
                    idx += 1
                    j += 2
                    if j == m-1:
                        tmp[idx] = tmp_board[j]
                        idx += 1
                else:
                    tmp[idx] = tmp_board[j]
                    idx += 1
                    tmp.append(tmp_board[j])
                    j += 1
                    if j == m-1:
                        tmp[idx] = tmp_board[j]
                        idx += 1

            if m == 1:
                tmp[idx] = tmp_board[0]
            for k in range(n):
                res[k][i] = tmp[k]

    if res == board:
        return []
    return res

def dfs(depth: int, board: list[list[int]]) -> None:
    if depth == 5:
        global ans
        ans = max(ans, max(map(max, board)))
        return
    
    for move in range(4):
        new = solve(move, board)
        if new:
            dfs(depth+1, new)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
ans = max(map(max, board))

dfs(0, board)

print(ans)