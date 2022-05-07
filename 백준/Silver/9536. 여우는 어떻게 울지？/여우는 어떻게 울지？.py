import sys
input = sys.stdin.readline
ano_ani = set()
t = int(input().rstrip())
for i in range(t):
    record = list(map(str, input().rstrip().split()))
    for j in range(100):
        animal = list(map(str, input().rstrip().split()))
        if animal[0] == "what":
            break
        else:
            ano_ani.add(animal[2])
    for k in record:
        if k not in ano_ani:
            print(k, end=" ")