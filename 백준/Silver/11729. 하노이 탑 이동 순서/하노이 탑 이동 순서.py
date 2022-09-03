def hanoi_top_move(n, start, end):
    if n == 1: # 마지막 원판
        print(start, end)
        return
    
    hanoi_top_move(n-1, start, 6-start-end) # 시작점에서 현재 시작점도 아니고 끝점도 아닌 마지막한곳
    print(start, end)
    hanoi_top_move(n-1, 6-start-end, end)

n = int(input())
print(2**n-1)
hanoi_top_move(n, 1, 3)