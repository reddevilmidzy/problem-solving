import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
pre = [int(input()) for _ in range(n)]
aft = [int(input()) for _ in range(m)]

a_idx, b_idx = 0, 0
load, cost = 0, 0

while a_idx < n and b_idx < m:
    if pre[a_idx] == 0:
        a_idx += 1
        continue

    elif aft[b_idx] == 0:
        b_idx += 1
        continue
    
    if pre[a_idx] < aft[b_idx]:
        load += pre[a_idx]
        cost += (a_idx+1 + b_idx+1) * pre[a_idx]
        aft[b_idx] -= pre[a_idx]
        a_idx += 1
    elif pre[a_idx] > aft[b_idx]:
        load += aft[b_idx]
        cost += (a_idx + 1 + b_idx + 1) * aft[b_idx]
        pre[a_idx] -= aft[b_idx]
        b_idx += 1
    elif pre[a_idx] == aft[b_idx]:
        load += aft[b_idx]
        cost += (a_idx + 1 + b_idx + 1) * pre[a_idx]
        pre[a_idx] = 0
        aft[b_idx] = 0
        a_idx += 1
        b_idx += 1

print(load, cost)