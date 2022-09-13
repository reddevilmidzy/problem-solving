import sys
input = sys.stdin.readline

def ccw(a1,b1,a2,b2,a3,b3):
    ans = (a2-a1)*(b3-b1)-(b2-b1)*(a3-a1)
    if ans > 0:
        return 1
    elif ans < 0:
        return -1
    else:
        return 0

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

print(ccw(x1,y1,x2,y2,x3,y3))