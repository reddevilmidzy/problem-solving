import sys
input = sys.stdin.readline
n = int(input())
han_num = 0
if len(str(n)) < 3:
    han_num = n
else:
    han_num = 99
    for i in range(100, n+1):
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            han_num += 1
print(han_num)