import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [0]*(n)

for i in range(1,m+1):
    l,r = map(int,input().split())
    for j in range(l-1, r):
        arr[j] = i

print(2**len(set(arr) - {0}))