n = int(input())
k = list(map(int,input().split()))
nums = [i for i in range(1, n+1)]
ans = []

if k == sorted(k):
    print(-1)
else:
    for i in range(n-1, 0, -1):
        if k[i] < k[i-1]:
            ans.extend(k[:i-1])
            tmp = k[i:]
            check = sorted(k[i:])[::-1]

            for j in range(len(check)):
                if check[j] < k[i-1]:
                    ans.append(check[j])
                    tmp.remove(check[j])
                    break
            tmp.append(k[i-1])
            ans.extend(sorted(tmp)[::-1])
            break
    print(*ans)