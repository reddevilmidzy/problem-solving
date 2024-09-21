import sys
input = sys.stdin.readline

n = int(input())
p = tuple(map(int,input().split()))
s = list(map(int,input().split()))


cur = []
for i in range(n//3):
    for j in range(3):
        cur.append(j)

v = set()
cur = tuple(cur)

def move(lis):
    tmp = [0]*n
    for i in range(n):
        nxt = s[i]
        tmp[nxt] = lis[i]    
    return tuple(tmp)

cnt = 0
while True:
    
    if p == cur:
        print(cnt)
        break
    
    nxt = move(p)
    if nxt not in v:
        v.add(nxt)
        p = nxt
    else:
        print("-1")
        break

    cnt += 1

