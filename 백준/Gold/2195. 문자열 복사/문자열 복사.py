import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

n,m = len(s), len(p)

st = dict()

for i in range(n):
    if s[i] not in st:
        st[s[i]] = []
    st[s[i]].append(i)

res = 0
idx = 0

while idx < m:
    tmp = idx
    for st_j in st[p[idx]]:
        i = idx
        j = st_j

        while i < m and j < n and p[i] == s[j]:
            i += 1
            j += 1
        tmp = max(tmp, i)
    idx = tmp
    res += 1
        
print(res)