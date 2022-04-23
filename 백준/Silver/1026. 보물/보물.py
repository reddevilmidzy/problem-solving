n= int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
result = 0

for i in range(n):
    result += a[i]*b[i]
print(result)