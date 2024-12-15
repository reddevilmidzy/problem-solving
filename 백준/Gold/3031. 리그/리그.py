import sys
input = sys.stdin.readline
INF = float('inf')
n = int(input())
res = []

# 경기수
def get_0(num: list[int]) -> int:
    return num[1] + num[2] + num[3]

# 이긴 수
def get_1(num: list[int]) -> int:
    if type(num[0] - num[2] - num[3]) != float:
        return num[0] - num[2] - num[3]
    return (num[4] - num[2]) // 3

# 비긴수
def get_2(num: list[int]) -> int:
    if type(num[0] - num[1] - num[3]) != float:
        return num[0] - num[1] - num[3]
    return num[4] - 3 * num[1]

# 진수
def get_3(num: list[int]) -> int:
    return num[0] - num[1] - num[2]

# 승점
def get_4(num: list[int]) -> int:
    return num[1]*3 + num[2]

for _ in range(n):
    tmp = list(input().rstrip().split())
    num = [int(i) if i!='?' else INF for i in tmp]

    if num.count(INF) == 0:
        pass 
    # 하나만 없는 경우
    # 경기수, 이긴수, 비긴수, 진수, 승점
    elif num.count(INF) == 1:
        if num[0] == INF:
            num[0] = get_0(num)
        elif num[1] == INF:
            num[1] = get_1(num)
        elif num[2] == INF:
            num[2] = get_2(num)
        elif num[3] == INF:
            num[3] = get_3(num)
        else:
            num[4] = get_4(num)

    # 두개 없는 경우
    # 경기수, 이긴수, 비긴수, 진수, 승점
    elif num.count(INF) == 2:
        if num[0] == INF and num[1] == INF:
            num[1] = get_1(num)
            num[0] = get_0(num)
        elif num[0] == INF and num[2] == INF:
            num[2] = get_2(num)
            num[0] = get_0(num)
        elif num[0] == INF and num[3] == INF:
            num[3] = 0
            num[0] = get_0(num)
            # 경기수랑 진수 모르면 불가능
            # 라고 생각했지만 꽉 채우면 될듯
        elif num[0] == INF and num[4] == INF:
            num[4] = get_4(num)
            num[0] = get_0(num)
        elif num[1] == INF and num[2] == INF:
            # 이긴수랑 비긴수를 모른다 하지만 승점을 알고 경기수를 알고 있기 때문에 구할 수 있을듯
            for win in range(num[0]+1):
                tie = num[0] - win - num[3]
                if win*3 + tie == num[4]:
                    num[1] = win
                    num[2] = tie
                    break
        elif num[1] == INF and num[3] == INF:
            num[1] = get_1(num)
            num[3] = get_3(num)
        elif num[1] == INF and num[4] == INF:
            num[1] = get_1(num)
            num[4] = get_4(num)
        
        elif num[2] == INF and num[3] == INF:
            num[2] = get_2(num)
            num[3] = get_3(num)
        elif num[2] == INF and num[4] == INF:
            num[2] = get_2(num)
            num[4] = get_4(num)
        
        elif num[3] == INF and num[4] == INF:
            num[4] = get_4(num)
            num[3] = get_3(num)
    
    # 세개 없는 경우
    # 경기수, 이긴수, 비긴수, 진수, 승점
    elif num.count(INF) == 3:
        if num[0] != INF and num[1] != INF:
           # 이 경우는 경기수랑 이긴수가 같을 수 밖에 없음
           # 왜냐 그게 유일하기때문ㅇ
           num[2] = 0
           num[3] = 0
           num[4] = get_4(num)
        elif num[0] != INF and num[2] != INF:
           # 역시 동일할 수밖에
           num[1] = 0
           num[3] = 0
           num[4] = get_4(num)
        elif num[0] != INF and num[3] != INF:
            num[1] = 0
            num[2] = 0
            num[4] = get_4(num)
        # 여기가 틀렸을지도
        elif num[0] != INF and num[4] != INF:
            num[1] = num[4]//3
            num[2] = num[4]%3
            num[3] = get_3(num)
       
        # 1,?,?,?,3 인 경우 알 수 있음 1,1,0,0,3
        # 2,?,?,?,3 인 경우 알 수 있음 2,1,0,1,3
        # 3,?,?,?,3 인 경우 구할 수 없음 3,0,3,0,3 or 3,1,0,2,3
        # 어쨋든 구할 수 있는 경우는 있는 것임
        # 유일한 경우만 입력 준다 했으니 하나 보이면 그거 출력하면 됨
        
        elif num[1] + num[2] == 100:
        # elif num[1] != INF and num[2] != INF:
            num[3] = 0
            num[4] = get_4(num)
            num[0] = 100
        elif num[1] + num[3] == 100:
            num[2] = 0
            num[4] = get_4(num)
            num[0] = 100
        elif num[1] != INF and num[4] != INF:
            for tie in range(101-num[1]):
                if num[1]*3 + tie == num[4]:
                    num[0] = 100
                    num[2] = tie
                    num[3] = get_3(num)
                    break
        elif num[2] + num[3] == 100:
            num[0] = 100
            num[1] = 0
            num[4] = get_4(num)
        
        
        elif num[2] != INF and num[4] != INF:
            for win in range(101-num[2]):
                if 3*win + num[2] == num[4]:
                    num[1] = win
                    num[0] = 100
                    num[3] = get_3(num)
                    break

        # 2 이하면 무승부갯수 나옴
        elif num[3] != INF and num[4] <= 2:
            num[2] = num[4]
            num[1] = 0
            num[0] = get_0(num)
        
        # 꽉꽉 채워서 얻을 수 있음
        elif num[3] != INF and num[4] != INF:
            # ? ? ? 1 297 반례
            # ? ? ? 99 1
            # ? ? ? 99 3

            for tot in range(100, -1, -1):
                if num[0] != INF:
                    break
                for win in range(tot+1-num[3]):
                    tie = tot - win - num[3]

                    if win*3+tie == num[4]:
                        num[1] = win
                        num[2] = tie
                        num[0] = get_0(num)
                        break
            else:
                di = dict()
                di['a'] += 1

    # 경기수가 0일수밖에 없음
    elif num[0] == 0:
        num[1] = 0
        num[2] = 0
        num[3] = 0
        num[4] = 0
    
    # 이긴수가 100일수밖에 없음
    elif num[1] == 100:
        num[0] = num[1]
        num[2] = 0
        num[3] = 0
        num[4] = get_4(num)

    # 비긴게 100일수밖에 없 
    elif num[2] == 100:
        num[0] = num[2]
        num[1] = 0
        num[3] = 0
        num[4] = get_4(num)
    
    # 진게 100일 수밖에
    elif num[3] == 100:
        num[0] = num[3]
        num[1] = 0
        num[2] = 0
        num[4] = get_4(num)
    elif num[4] != INF:
        for win in range(101):
            tie = 100 - win
            if win*3 + tie == num[4]:
                num[1] = win
                num[2] = tie
                num[3] = 0
                num[0] = 100
                break
        else:
            raise AssertionError
    res.append(num)

for ans in res:
    # if INF in ans:
        # raise KeyError
    print(*ans)

# 9 2 3 4 10