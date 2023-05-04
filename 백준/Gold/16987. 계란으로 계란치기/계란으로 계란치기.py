import sys
input = sys.stdin.readline

def bt(cur: int, eggs:list[list[int]], cnt: int):
    global ans
    ans.append(cnt)

    # 가장 오른 쪽 놈이라면
    if cur == n:
        return

    # 손에 든 게 깨졌다면
    if eggs[cur][0] <= 0:
        # print("여기 옴?")
        bt(cur+1, eggs,cnt)
    else:
        for i in range(n):
            if i == cur:
                continue
            if eggs[i][0] > 0: # 아직 안깨짐
                eggs[i][0] -= eggs[cur][1] # 무게만큼 빼기
                eggs[cur][0] -= eggs[i][1]

                # 둘 다 깨짐
                if eggs[i][0] <= 0 and eggs[cur][0] <= 0:
                    bt(cur+1, eggs, cnt+2)
                
                # 손에 쥐고 있는게 깨짐
                # 오른쪽으로 하나 이동
                elif eggs[cur][0] <= 0:
                    bt(cur+1, eggs, cnt+1)
                # 맞은 놈이 깨짐, 들고 있는건 계속 들고 있음
                elif eggs[i][0] <= 0:
                    bt(cur+1, eggs, cnt+1)
                else:
                    bt(cur+1, eggs, cnt)

                eggs[cur][0] += eggs[i][1]
                eggs[i][0] += eggs[cur][1] # 무게만큼 더하기

n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)] # 내구도, 무게 (s,w)
ans = []
bt(0, eggs, 0)
print(max(ans))