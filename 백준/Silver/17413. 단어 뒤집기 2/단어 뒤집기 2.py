word = list(input())

right = False
revers = []
for i in word:
    if i == "<":
        if len(revers) != 0:
            print("".join(revers)[::-1], end="")
            revers = []
        print(i, end="")
        right = True
    elif i == ">":
        print(i, end="")
        right = False
    elif right == False and i != " ": revers.append(i)
    elif right == False and i == " ":
        print("".join(revers)[::-1], end=" ")
        revers = []
    elif right == True: print(i, end="")

if len(revers) != 0:
    print("".join(revers)[::-1])