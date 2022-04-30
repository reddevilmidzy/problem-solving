ex = []
cnt = 0
n = int(input())
for i in range(n): ex.append(int(input()))

for j in range(n-2, -1, -1):
    if ex[j] >= ex[j+1]:
        cnt += ex[j] - ex[j+1] + 1
        ex[j] = ex[j+1] - 1

print(cnt)