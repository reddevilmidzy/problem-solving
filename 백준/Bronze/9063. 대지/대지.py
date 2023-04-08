import sys
input=sys.stdin.readline
INF=10**5
min_x,max_x,min_y,max_y=INF,-INF,INF,-INF
for _ in range(int(input())):
    x,y = map(int,input().split())
    min_x,max_x=min(min_x,x),max(max_x,x)
    min_y,max_y=min(min_y,y),max(max_y,y)
print(abs(max_y-min_y)*abs(max_x-min_x))