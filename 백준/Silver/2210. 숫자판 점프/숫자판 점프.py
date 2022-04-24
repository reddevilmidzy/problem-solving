import sys
from itertools import product

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

fan = [list(map(int, input().rstrip().split())) for i in range(5)]
result = []
for j in range(5):
    for k in range(5):
        for dir in product(range(4), repeat=5):
            temp = []
            temp.append(fan[j][k])
            x, y = j, k
            for o in dir:
                x, y = x + dx[o] , y + dy[o]
                if not (0 <= x < 5 and 0 <= y < 5):
                    break
                temp.append(fan[x][y])
            if len(temp) == 6:
                result.append("".join(map(str, temp)))

print(len(set(result)))                

