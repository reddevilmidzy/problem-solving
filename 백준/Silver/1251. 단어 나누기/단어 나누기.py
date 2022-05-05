n = list(input())
fore = "z"*50
for i in range(len(n)-2):
    for j in range(i+1, len(n)-1):
        if fore > "".join(list(reversed(n[:i+1])))+"".join(list(reversed(n[i+1:j+1])))+"".join(list(reversed(n[j+1:]))):
            fore = "".join(list(reversed(n[:i+1])))+"".join(list(reversed(n[i+1:j+1])))+"".join(list(reversed(n[j+1:])))

print(fore)