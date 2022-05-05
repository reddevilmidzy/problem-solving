div = [i for i in range(1, 4473)]
n = int(input())
cnt = 1
for d in div:
    if n - d <= 0:
        cnt += 1
        if d%2 == 0:
            print(f"{n}/{cnt-n}")
        else:
            print(f"{cnt-n}/{n}")
        break
    else:
        n -= d
        cnt += 1
