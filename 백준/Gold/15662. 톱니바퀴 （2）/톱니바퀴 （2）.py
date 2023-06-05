from collections import deque
import sys
input = sys.stdin.readline

def move(num, wise):
    bool_list = []
    # 2: 3시 방향, 6: 9시 방향
    for i in range(t-1):
        bool_list.append(gears[i][2] != gears[i+1][6])
    
    # 현재꺼 회전
    gears[num].rotate(wise)
    tmp = wise
    for right in range(num, t-1):
        if bool_list[right]:
            tmp *= -1
            gears[right+1].rotate(tmp)
        else:
            break
    
    for left in range(num-1, -1, -1):
        if bool_list[left]:
            wise *= -1
            gears[left].rotate(wise)
        else:
            break

t = int(input())
gears = [deque(list(map(int,input().rstrip()))) for _ in range(t)]

k = int(input())
for _ in range(k):
    num, wise = map(int,input().split())
    move(num-1, wise)
print(sum([i.popleft() for i in gears]))