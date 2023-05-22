n = int(input())
answer = [[], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for i in range(2, n+1):
    temp = []
    for j in range(10):
        if j == 0:
            temp.append(answer[i - 1][1])
        elif j == 9:
            temp.append(answer[i - 1][8])
        else:
            temp.append(answer[i - 1][j - 1] + answer[i - 1][j + 1])
    answer.append(temp)
print(sum(answer[n])%1000000000)