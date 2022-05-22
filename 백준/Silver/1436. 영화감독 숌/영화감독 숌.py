arr = [str(i) for i in range(2666800)]
cnt = 0
n =int(input())
for j in arr:
    if "666" in j:
        cnt += 1

    if n == cnt:
        print(j)
        break