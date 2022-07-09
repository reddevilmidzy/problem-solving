import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().rstrip().split()))
s = int(input())

while True:
    tof = False
    for i in range(n):
        idx = i
        cmp = 0
        for j in range(n-1, i, -1):
            if arr[idx] < arr[j] and j-i <= s:
                idx = j
                tof = True
                cmp = j-i
        if idx != i:
            tmp=arr[idx]
            del arr[idx]
            arr.insert(i,tmp)
            s -= cmp
            break
    if not tof:
        break
print(*arr)