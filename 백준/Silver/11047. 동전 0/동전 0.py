n, k = map(int, input().split())
cnt = 0
arr = []
for i in range(n):
    coin = int(input())
    arr.append(coin)
arr.reverse()

for i in arr:
    # print(i)
    if k//i >= 1:
        cnt += k//i
        k = k%i
print(cnt)