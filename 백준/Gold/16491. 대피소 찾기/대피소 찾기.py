from itertools import permutations
def ccw(a1,b1,a2,b2,a3,b3):
    tmp = (a2-a1)*(b3-b1)-(b2-b1)*(a3-a1)
    if tmp > 0: # 반시계
        return 1
    if tmp < 0: # 시계
        return -1
    return 0    # 평행

def cross(x1,y1,x2,y2,x3,y3,x4,y4):
    first = ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)
    second = ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)
    
    if first == 0 and second == 0:
        return max(x1,x2) >= min(x3,x4) and max(x3,x4) >= min(x1,x2) and \
                max(y1,y2) >= min(y3,y4) and max(y3,y4) >= min(y1,y2)
    return first <= 0 and second <= 0

def solve(order):
    for i in range(n):
        for j in range(i+1,n):
            if cross(*robot[i], *shelter[order[i]],*robot[j], *shelter[order[j]]):
                return False
    return True

n = int(input())
robot = [list(map(int,input().split())) for _ in range(n)]
shelter = [list(map(int,input().split())) for _ in range(n)]

for i in permutations(range(n),n):
    if solve(i):
        for j in i:print(j+1)
        break