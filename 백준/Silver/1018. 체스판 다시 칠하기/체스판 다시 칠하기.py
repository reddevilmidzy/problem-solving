n, m = map(int, input().split())

chess = [input() for i in range(n)]
check = []

for j in range(n-7):
    for k in range(m-7):
        first_w = 0
        first_b = 0
        for a in range(j, j+8):
            for b in range(k, k+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != "W":
                        first_w += 1
                    if chess[a][b] != "B":
                        first_b += 1
                else:
                    if chess[a][b] != "B":
                        first_w += 1
                    if chess[a][b] != "W":
                        first_b += 1
        check.append(first_w)
        check.append(first_b)
print(min(check))