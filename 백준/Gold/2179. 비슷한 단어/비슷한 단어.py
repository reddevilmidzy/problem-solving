n = int(input())
a = [input() for _ in range(n)]
b = sorted(list(enumerate(a)),key = lambda x: x[1])

def sol(a, b):
    cnt = 0
    m = min(len(a), len(b))
    for i in range(m):
        if a[i] == b[i]: cnt += 1
        else: break
    return cnt

length = [0] * (n+1)
maxlength = 0

for i in range(n-1):
    if b[i][1] == b[i+1][1]: continue
    tmp = sol(b[i][1], b[i+1][1])
    maxlength = max(maxlength, tmp)
        
    length[b[i][0]] = max(length[b[i][0]], tmp)
    length[b[i+1][0]] = max(length[b[i+1][0]], tmp)

first = 0
for i in range(n):
    if first == 0:
        if length[i] == max(length):
            first = a[i]
            print(first)
            pre = a[i][:maxlength]
    else:
        if length[i] == max(length) and a[i][:maxlength] == pre:
            print(a[i])
            break