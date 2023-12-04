n,k=map(int,input().split())
a=list(map(int,input().split()))
print(n*(2*(a[0]+max([a[i]-i*k-a[0]for i in range(n)]))+(n-1)*k)//2-sum(a))