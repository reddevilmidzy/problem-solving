submit = {i for i in range(1, 31)}
check = {int(input()) for i in range(28)}
print(*sorted(submit-check), sep="\n")