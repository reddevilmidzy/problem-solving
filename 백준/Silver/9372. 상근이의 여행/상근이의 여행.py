import sys
input = sys.stdin.readline

for test in range(int(input().rstrip())):
    n,m = map(int, input().rstrip().split())
    road = [input() for i in range(m)]
    print(n-1)