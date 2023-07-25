import sys
input = sys.stdin.readline

radian = [9,36,81,144,225]
point = [100, 80, 60, 40, 20]

def get_point(arr:list[float]) -> int:
    res = 0
    for i in range(0,len(arr),2):
        x,y = arr[i],arr[i+1]
        dist = x**2 + y**2
        for j in range(5):
            if dist <= radian[j]:
                res += point[j]
                break
    return res

t = int(input())

for _ in range(t):
    tmp = list(map(float, input().rstrip().split()))
    p1,p2 = get_point(tmp[:6]),get_point(tmp[6:])
    if p1==p2:res ="TIE"
    elif p1 > p2: res = "PLAYER 1 WINS"
    else: res = "PLAYER 2 WINS"

    print(f"SCORE: {p1} to {p2}, {res}.")