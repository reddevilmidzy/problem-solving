def collocate(r: int, c: int, num: int) -> bool:
    for x in range(n):
        if board[r][x] == num: return False

    for y in range(n):
        if board[y][c] == num: return False
    
    for y in range((r//3)*3, (r//3)*3+3):
        for x in range((c//3)*3, (c//3)*3+3):
            if board[y][x] == num: return False
    
    return True

def bt(s: list[int], idx: int):
    if len(s) == len(zero):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end='')
            print()
        exit()
    for num in nums:
        r,c = zero[idx][0], zero[idx][1]
        if collocate(r, c, num):
            s.append(num)
            board[r][c] = num
            bt(s, idx+1)
            board[r][c] = 0
            s.pop()

n = 9
board = [list(map(int,input().rstrip())) for _ in range(n)]
nums = [i for i in range(1, n+1)]

zero = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            zero.append((i,j))

bt([], 0)