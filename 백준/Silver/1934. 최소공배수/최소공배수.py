import sys
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    a, b = map(int, input().rstrip().split())
    for j in range(max(a,b), 0, -1):
        if a%j == 0 and b%j == 0:
            print(a*b//j)
            break