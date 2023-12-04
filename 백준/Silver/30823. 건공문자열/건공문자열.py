n,k = map(int,input().split())
s = input().rstrip()
if (n-k)%2:
    print(s[k-1:] + s[:k-1])
else:
    print(s[k-1:] + s[:k-1][::-1])