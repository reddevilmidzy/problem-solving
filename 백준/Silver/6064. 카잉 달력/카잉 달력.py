import sys
input = sys.stdin.readline

def solution(m,n,x,y):
    while x <= m*n:
        if (x-y)%n == 0:
            return x
        x += m
    return -1

n =int(input())
for _ in range(n):
    m,n,x,y = map(int,input().rstrip().split())
    print(solution(m,n,x,y))