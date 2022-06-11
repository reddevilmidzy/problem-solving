n = int(input())
dp =[3,7]
for i in range(3, n+1):
    one = dp.pop()
    two = dp.pop()
    dp.append(one)
    dp.append(one*2+two)
print(dp[-1]%9901) if n != 1 else print(3)