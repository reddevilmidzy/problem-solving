while True:
    test = True
    hochul = False
    stk = []
    s = input()
    if len(s) == 1 and s == ".":
        break
    
    for i in s:
        if i == "(":
            stk.append(i)
        elif i == "[":
            stk.append(i)
        elif i == ")":
            if len(stk) != 0:
                a = stk.pop()
                if a != "(":
                    print("no")
                    hochul = True
                    test = False
                    break
            else:
                print("no")
                hochul = True
                test = False
                break
        elif i == "]":
            if len(stk) != 0:
                a = stk.pop()
                if a != "[":
                    print("no")
                    hochul = True
                    test = False
                    break
            else:
                print("no")
                hochul = True
                test = False
                break
    if len(stk) == 0 and test == True:
        print("yes")
    elif hochul == False:
        print("no")