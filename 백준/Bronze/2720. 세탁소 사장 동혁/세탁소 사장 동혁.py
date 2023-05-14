import sys
input = sys.stdin.readline

def solve(c:int) -> list[int]:
    res = []
    for i in [25,10,5,1]:
        res.append(c//i)
        c%=i
    return res

for _ in range(int(input())):
    c = int(input())
    print(*solve(c))