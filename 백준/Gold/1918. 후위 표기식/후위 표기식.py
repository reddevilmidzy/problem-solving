pieonsan = {"/":2, "*":2, "+":1, "-":1, "(":0}
stk = []
sick = list(input())

for i in sick:
    if i.isalpha(): print(i, end="")
    elif i == "(": stk.append(i)
    elif i ==")":
        while True:
            tmp = stk.pop()
            if tmp == "(":
                break
            print(tmp, end="")
    else:
        while stk and pieonsan[stk[-1]] >= pieonsan[i]:
            print(stk.pop(), end="")
        stk.append(i)
while stk:
    print(stk.pop(), end="")