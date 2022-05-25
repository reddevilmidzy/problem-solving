import sys

input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    num1, num2 = map(str, input().rstrip().split())
    num1 = int(num1, 2)
    num2 = int(num2, 2)
    ans = str(bin(num1 + num2))
    print(ans[2:])