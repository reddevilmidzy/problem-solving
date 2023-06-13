from collections import Counter
from sys import stdin

input = stdin.readline

n = int(input())
origin = "".join(sorted(input().rstrip()))
cnt  = Counter(origin)
m = len(origin)
ans = 0
for _ in range(n-1):
    word = "".join(sorted(input().rstrip()))
    k = len(word)
    canbe = True
    tmp = Counter(word)
    cnt_keys = cnt.keys()
    tmp_keys = tmp.keys()

    if origin == word:
        ans += 1
    elif m - k == 0 and (len(set(cnt_keys) - set(tmp_keys)) <= 1 or len(set(tmp_keys) - set(cnt_keys)) <= 1): # 둘이 길이 같음
        change1 = 0
        for key in cnt_keys:
            if key in tmp:
                if cnt[key] == tmp[key]: pass
                elif abs(cnt[key] - tmp[key]) == 1: # 하나 차이
                    change1 += 1
                else:
                    canbe = False
                    break
            elif cnt[key] == 1: # 없다면
                change1 += 1
            else:
                canbe = False
                break

        change2 = 0

        for key in tmp_keys:
            if key in cnt:
                if cnt[key] == tmp[key]: pass
                elif abs(cnt[key] - tmp[key]) == 1: # 하나 차이
                    change2 += 1
                else:
                    canbe = False
                    break
            elif tmp[key] == 1: # 없다면
                change2 += 1
            else:
                canbe = False
                break
        
        if not canbe or change1 > 2 or change2 > 2: continue
        if change1==2 or change2==2 or change1+change2==2:
            ans += 1

    elif abs(m-k) == 1: # 하나 차이, 새로운거 추가

        change1 = 0
        for key in cnt_keys:
            if key in tmp:
                if cnt[key] == tmp[key]: pass
                elif abs(cnt[key] - tmp[key]) == 1: # 하나 차이
                    change1 += 1
                else:
                    canbe = False
                    break
            elif cnt[key] == 1: # 없다면
                change1 += 1
            else:
                canbe = False
                break

        change2 = 0
        for key in tmp_keys:
            if key in cnt:
                if cnt[key] == tmp[key]: pass
                elif abs(cnt[key] - tmp[key]) == 1: # 하나 차이
                    change2 += 1
                else:
                    canbe = False
                    break
            elif tmp[key] == 1: # 없다면
                change2 += 1
            else:
                canbe = False
                break

        if not canbe or change1 > 1 or change2 > 1: continue
        if change1==1 or change2==1:
            ans += 1
    
print(ans)