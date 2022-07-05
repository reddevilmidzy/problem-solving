n = int(input())
if n > 2**10-2:
    print(-1)
else:
    val = 0 # 증가시킬 값
    order = 0 # 순서 확인 할 거  n == order
    while True:
        if order == n:
            print(val)
            break
        else:
            val = int(val)
            val += 1
            val = str(val)
            for i in range(len(val)-1):
                if val[i] > val[i+1]:
                    pass
                else:
                    val = int(val[:i] + str(int(val[i])+1) + '0'*(len(val)-i-1))-1
                    break
            else:
                order += 1