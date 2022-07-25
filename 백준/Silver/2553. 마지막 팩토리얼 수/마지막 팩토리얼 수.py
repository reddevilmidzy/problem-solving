import math
n=str(math.factorial(int(input())))
idx=-1
while True:
    if n[idx]!='0':
        print(n[idx])
        break
    idx -=1