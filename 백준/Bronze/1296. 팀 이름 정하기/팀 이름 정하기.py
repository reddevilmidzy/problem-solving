green = input()
candi = dict()

l= green.count("L")
o= green.count("O")
v= green.count("V")
e= green.count("E")

for i in range(int(input())):
    name =  input()
    L = name.count("L") + l
    O = name.count("O") + o
    V = name.count("V") + v
    E = name.count("E") + e
    candi[name] = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E))%100
win = max(candi.values())
for val, key in sorted(candi.items()):
    if key == win:
        print(val)
        break