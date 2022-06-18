import sys
input = sys.stdin.readline
money = 0
while True:
    bat = int(input())
    if bat != -1:
        money += bat
    else:
        print(money)
        break