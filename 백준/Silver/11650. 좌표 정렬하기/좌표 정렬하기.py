import sys

input = sys.stdin.readline
coordinate = []
n = int(input().rstrip())

for i in range(n):
    x, y = map(int, input().rstrip().split())
    pos = [x, y]
    coordinate.append(pos)

for i in sorted(coordinate): print(i[0], i[1])