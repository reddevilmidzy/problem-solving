def hanoi_top_move(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi_top_move(n-1, start, 6-start-end)
    print(start, end)
    hanoi_top_move(n-1, 6-start-end, end)

def hanoi_top_cnt(n):
    if n == 1:
        return 1
    else:
        return hanoi_top_cnt(n-1)*2 + 1

n = int(input())
print(hanoi_top_cnt(n))
hanoi_top_move(n, 1, 3)