import sys
input = sys.stdin.readline
s = set()
for i in range(int(input())):
    code = input()
    if code[:3] == "add":
        code, num = code.split()
        s.add(int(num))
    elif code[:5] == "check":
        code, num = code.split()
        if int(num) in s:
            print(1)
        else:
            print(0)
    elif code[:6] == "remove":
        code, num = code.split()
        if int(num) in s:
            s.remove(int(num))
    elif code[:6] == "toggle":
        code, num = code.split()
        if int(num) in s:
            s.remove(int(num))
        else:
            s.add(int(num))
    elif code[:3] == "all":
        s = {i for i in range(1, 21)}
    else:
        s = set()