n,k=map(int,input().split())
s=input()
print(s[k-1:],end='')
print(s[:k-1] if (n-k)%2 else s[:k-1][::-1])