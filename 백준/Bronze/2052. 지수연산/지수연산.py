a = int(input())
a = "%.250f" % (1/(2**a))

for i in range(len(a)-1, -1, -1):
    if a[i] != "0":
        print(a[:i+1])
        break