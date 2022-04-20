import sys

input = sys.stdin.readline
coordinate = []
n = int(input().rstrip())

for i in range(n):
    x, y = map(int, input().rstrip().split())
    pos = [x, y]
    coordinate.append(pos)
coordinate.sort()

for i in range(n):
    print(coordinate[i][0], coordinate[i][1])