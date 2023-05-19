from itertools import combinations
import sys
input = sys.stdin.readline
def hypo(x: list[int], y: list[int]) -> int:
    return (x[0] - y[0])**2 + (x[1] - y[1])**2

def validate(a: list[int], b: list[int], c: list[int]) -> bool:
    A,B,C = hypo(a,b), hypo(b,c), hypo(c,a)
    return A+B==C or B+C==A or C+A==B
n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if validate(points[i], points[j], points[k]):
                ans += 1
print(ans)