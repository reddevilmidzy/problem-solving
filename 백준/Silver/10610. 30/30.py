n = list(input())
n.sort(reverse=True)
ans = int(''.join(n))
print(ans) if ans%30 == 0 else print(-1) 