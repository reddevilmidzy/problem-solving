import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
A = [list(map(int,input().rstrip().split())) for i in range(n)]
B = [list(map(int,input().rstrip().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j],end=' ')
    print()