import sys
input=sys.stdin.readline
inf=4*(10**9)+7
for _ in range(int(input())):
    n=int(input())
    if n <= 2:
        print(2)
    else:
        for i in range(n, inf+1):
            for j in range(2, int(n**0.5)+2):
                if i%j==0:
                    break
            else:
                print(i)
                break