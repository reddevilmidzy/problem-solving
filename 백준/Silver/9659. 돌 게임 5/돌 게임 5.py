n = int(input())
div = n//3
mod = n%3

if mod==1:
    print(["CY","SK"][div%2!=1])
else:
    print(["CY","SK"][div%2==1])