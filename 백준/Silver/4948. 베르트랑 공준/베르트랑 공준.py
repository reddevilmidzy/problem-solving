import sys
input = sys.stdin.readline

m = 123456
arr = [True for i in range(1, m*2+2)]
arr[0], arr[1] = False, False

for i in range(2, int((m*2)**0.5)+2):
    if arr[i]:
        j = 2
        while i * j <= 2*m:
            arr[i*j] = False
            j += 1

#print(arr)
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if arr[i]:
            cnt += 1
    print(cnt)