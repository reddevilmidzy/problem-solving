money = int(input())
cnt = 0

money = 1000 - money
remind_money = [500,100,50,10,5,1]

for i in remind_money:
    cnt += money//i
    money = money%i
print(cnt)