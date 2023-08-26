import sys
input = sys.stdin.readline

def update(idx, n, tree):
    while idx <= n:
        tree[idx] += 1
        idx += (idx&-idx)

def query(idx, tree):
    res = 0
    while idx > 0:
        res += tree[idx]
        idx -= (idx&-idx)
    return res

n = int(input())
tree = [0]*(n+1)
edges = []
a = list(map(int,input().split()))
nums = {a[i]:i+1 for i in range(n)}
b = list(map(int,input().split()))

for i in range(n):
    a_idx = nums[b[i]]
    edges.append((a_idx<<32)|(i+1))

edges.sort()
res = 0
for i in range(n-1,-1,-1):
    b = edges[i] & ((1 << 32) -1)
    res += query(b-1, tree)
    update(b, n, tree)

print(res)