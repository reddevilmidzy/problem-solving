import sys
input = sys.stdin.readline

while True:
    a,b = map(int,input().split())
    if not a: break
    if a%b == 0 or b%a == 0:print(["factor", "multiple"][a>b])
    else:print("neither")
