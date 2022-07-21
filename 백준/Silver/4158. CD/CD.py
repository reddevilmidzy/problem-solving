import sys
input = sys.stdin.readline

def binary(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0

while True:
    n, m = map(int, input().rstrip().split())
    n_num = []
    cnt = 0
    if n+m == 0:
        break
    else:
        n_num = [int(input().rstrip()) for i in range(n)]
        for j in range(m):
            cnt += binary(n_num, int(input().rstrip()), 0, n-1)
    print(cnt)  