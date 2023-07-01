from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    n=int(input())
    print((n*(n+6)+12)//12)