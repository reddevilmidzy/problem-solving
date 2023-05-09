import sys
input = sys.stdin.readline
def solve():
    note = set(input().rstrip() for _ in range(n))
    for _ in range(m):
        note -= set(map(str,input().rstrip().split(",")))
        print(len(note))
n,m = map(int,input().split())
solve()