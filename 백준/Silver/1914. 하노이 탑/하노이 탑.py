def hanoi_top_move(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi_top_move(n-1, start, 6-start-end)
    print(start, end)
    hanoi_top_move(n-1, 6-start-end, end)

n = int(input())
if n > 20:
    print(2**n-1)
else:
    print(2**n-1)
    hanoi_top_move(n, 1, 3)