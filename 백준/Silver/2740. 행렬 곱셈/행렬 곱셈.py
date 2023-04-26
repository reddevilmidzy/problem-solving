import sys
input = sys.stdin.readline

def product(A:list[list[int]], B:list[list[int]]):
    return [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
m,k = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(m)]

for x in product(a, b):
    print(*x)