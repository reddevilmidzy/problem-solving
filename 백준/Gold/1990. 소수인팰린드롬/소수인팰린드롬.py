def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

a,b=map(int,input().split())
if a%2==0:
    a+=1
candy=[i for i in range(a,b+1,2) if str(i)==str(i)[::-1]]
for j in candy:
    if prime(j):
        print(j)
print(-1)