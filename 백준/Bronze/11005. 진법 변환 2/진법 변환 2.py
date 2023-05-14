n,b = map(int,input().split())
ans = []
while n:
    ans.append(str(n%b) if n%b < 10 else chr(n%b+55))
    n //= b
print("".join(reversed(ans)))