import sys
input = sys.stdin.readline

try:
    while True:
        n = int(input().rstrip())
        i = 1
        while True:
            if int("1"*i)%n == 0:
                print(i)
                break
            i += 1
except:
    exit()