import sys
input = sys.stdin.readline

n = int(input())

max_res = [0,0,0]
min_res = [0,0,0]

max_tmp = [0,0,0]
min_tmp = [0,0,0]

for _ in range(n):
    l,c,r = map(int,input().split())
    
    max_tmp[0] = max(max_res[0], max_res[1]) + l
    max_tmp[1] = max(max_res) + c
    max_tmp[2] = max(max_res[1], max_res[2]) + r

    min_tmp[0] = min(min_res[0], min_res[1]) + l
    min_tmp[1] = min(min_res) + c
    min_tmp[2] = min(min_res[1], min_res[2]) + r

    for i in range(3):
        max_res[i] = max_tmp[i]
        min_res[i] = min_tmp[i]

print(max(max_res), min(min_res))