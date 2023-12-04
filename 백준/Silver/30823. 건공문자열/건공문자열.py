n,k=map(int,input().split())
s=input()
k-=1
print(s[k:],end=s[:k][::-1]if (n-k)%2 else s[:k])