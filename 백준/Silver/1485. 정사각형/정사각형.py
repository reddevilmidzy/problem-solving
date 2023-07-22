import sys
input = sys.stdin.readline

def dist(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2

def validate(arr):
    arr.sort()
    return arr[0] + arr[1] == arr[2]

t = int(input())
for _ in range(t):
    p = [list(map(int,input().split())) for _ in range(4)]
    lines = sorted([dist(p[i], p[j]) for i in range(4) for j in range(i+1, 4)])
    print(1 if len(set(lines[:4])) == 1 and len(set(lines[4:])) == 1 else 0)
