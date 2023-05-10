s = list(input())
n = len(s)
cnt = dict()
for c in s:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1

if max(cnt.values()) > (n+1)//2:
    print(-1)
else:
    s.sort()

    for i in range((n+1)//2, n): # 홀수일때 중앙값 무시하기 위해
        if s[i] != s[n-i-1]:
            continue
        for j in range(i, n):
            if s[i] != s[j]:
                s[i], s[j] = s[j], s[i]
                break
    print("".join(s))