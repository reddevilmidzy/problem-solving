import sys
input = sys.stdin.readline

def solve(x:int, y:int) -> str: 
    if x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"
    else:
        return "AXIS"    

while True:
    x,y = map(float,input().split())
    print(solve(x,y))
    if x == 0 and y == 0:
        break