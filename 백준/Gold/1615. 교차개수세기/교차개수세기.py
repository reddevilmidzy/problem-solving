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

def solve():
    n,m = map(int,input().split())
    tree = [0]*(n+1)
    edges = []
    for _ in range(m):
        a,b = map(int,input().split())
        edges.append((a<<32)|b)

    edges.sort()
    res = 0

    for i in range(m-1,-1,-1):
        b = edges[i] & ((1 << 32) -1)
        res += query(b-1, tree)
        update(b, n, tree)

    return res

if __name__ == "__main__":
    print(solve())