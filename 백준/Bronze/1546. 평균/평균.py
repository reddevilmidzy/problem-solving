N = int(input())
a = (input().split())
ave = 0
for i in range(N):
  a[i] = int(a[i])
max_num = max(a)

for i in range(N):
  a[i] = a[i]/max_num*100

for i in range(N):
  ave = ave+a[i]  
print(ave/N)