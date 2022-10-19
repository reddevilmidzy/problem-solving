import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    r,c = map(int,input().split())
    k=min(r,c)-1
    n_1 = k*(k+1)//2
    n_2 = (k*(k+1)*(2*k+1))//6
    print(r*c*k*2+r*c+2*(-n_1*r)+2*(-n_1*c)+n_2*2,r*c*k*2+r*c+2*(-n_1*r)+2*(-n_1*c)+n_2*2-min(r,c))