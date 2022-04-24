import sys
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    h, w, n = map(int, input().rstrip().split())
    cnt = 0
    dong = 0
    ho = 0
    while True:    
        if n - h > 0:
            n -= h
            cnt += 1
        else:
            dong = n
            ho = cnt+1
            break
    print(str(dong)+str(ho).zfill(2))