n = int(input())

def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

if n==1 or n==2:
    print(2)
else:
    if n%2==0:
        n+=1
    candy=[i for i in range(n,1003002,2) if str(i)==str(i)[::-1]]
    for j in candy:
        if prime(j):
            print(j)
            break