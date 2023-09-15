n = 8
s = [input() for _ in range(n)]
p = {"K":0, "k":0, "P":1,"p":1,"N":3,"n":3,"B":3,"b":3,"R":5,"r":5,"Q":9,"q":9}
b = 0
w = 0

for i in range(n):
    for j in range(n):
        if s[i][j] != ".":
            if s[i][j].isupper():
                w += p[s[i][j]]
            else:
                b += p[s[i][j]]
print(w-b)