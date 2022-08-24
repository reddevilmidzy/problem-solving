import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int,input().split()))
m = int(input())
for _ in range(m):
    sex,num = map(int,input().split())
    if sex == 1:
        for i in range(num-1, n,num):
            switch[i] = switch[i]^1
            # print(i)
    else:
        num -= 1
        w = 0
        while True:
            if num - w > -1 and num + w < n:
                if switch[num-w]==switch[num+w]:
                    w+= 1
                else: # 더 이상 가능하는거 아님
                    break
            else: # while 문끝내는
                break
        w -= 1
        for i in range(num-w, num+w+1):
            switch[i] = switch[i]^1

if n > 20:
    idx = 0
    for i in range(n//20):
        for j in range(20):
            print(switch[idx],end=' ')
            idx += 1
        print()
    for k in range(n%20):
        print(switch[idx], end=' ')
        idx += 1
else:
    print(*switch)