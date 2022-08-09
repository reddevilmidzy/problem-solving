import sys
input = sys.stdin.readline

n,m = map(int,input().split())
string = [list(map(int,input().split())) for _ in range(m)]
six = sorted(string, key=lambda x:x[0])[0][0]
one = sorted(string, key=lambda x:x[1])[0][1]

if n < 6:
    print(min(six, one*n))
else:
    if six<one*6:
        print(min((n//6+1)*six, (n//6)*six+(n%6)*one))
    else:
        print(n*one)
#print(six, one)