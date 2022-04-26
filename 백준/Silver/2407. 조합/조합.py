import math
m, n = map(int, input().split())
print(math.factorial(m)//math.factorial(m-n)//math.factorial(n))