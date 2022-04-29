import sys, math
input = sys.stdin.readline
five = [5**i for i in range(1, 7)]
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    cnt = 0
    if n < 5:
        print(str(math.factorial(n))[-1])
    else:
        answer = str(math.factorial(n))
        for f in five:
            cnt += n//f
        print(answer[len(answer)-1-cnt:-cnt])