n = int(input())
cnt = 1
for i in range(1, 18259):
    if n <= cnt:
        print(i)
        break
    cnt += 6*i