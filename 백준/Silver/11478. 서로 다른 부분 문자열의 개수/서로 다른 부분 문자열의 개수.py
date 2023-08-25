s=input().rstrip();n=len(s)
print(len({s[i:j] for i in range(n) for j in range(i+1, n+1)}))