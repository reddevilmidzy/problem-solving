s, bomb = input(), input()
last_bomb = bomb[-1]
stk = []
for string in s:
    stk.append(string)
    if string == last_bomb and "".join(stk[-len(bomb):]) == bomb:
        del stk[-len(bomb):]
print("".join(stk)) if len(stk) != 0 else print("FRULA")