n =int(input())
for i in range(n): print(" "*((n-1)-i)+"*"*i+"*"+"*"*i)
for i in range(n-2,-1,-1): print(" "*((n-1)-i)+"*"*i+"*"+"*"*i)