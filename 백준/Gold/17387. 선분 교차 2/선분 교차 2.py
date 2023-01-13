import sys
input = sys.stdin.readline

def ccw(a1,b1,a2,b2,a3,b3):
    tmp = (a2-a1)*(b3-b1)-(b2-b1)*(a3-a1)
    if tmp>0: # 반시계 방향
        return 1
    elif tmp<0: # 시계 방향
        return -1
    else: # 평행
        return 0

def solve():
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3,x4,y4 = map(int,input().split())

    first = ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)
    second = ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)
    if first == 0 and second == 0:
        return max(x1,x2) >= min(x3,x4) and max(x3,x4) >= min(x1,x2) and max(y1,y2) >= min(y3,y4) and max(y3,y4) >= min(y1,y2)
    return first <= 0 and second <= 0

print(1 if solve() else 0)