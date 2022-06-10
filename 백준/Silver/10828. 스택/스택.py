import sys
n = int(sys.stdin.readline().rstrip())
sta = []
def push(ord):
    com, num = ord.split()
    sta.append(num)
    return sta

def top():
    if len(sta) != 0:
        print(sta[-1])
    elif len(sta) == 0:
        print(-1)

def pop():
    if len(sta) != 0:
        print(sta.pop())
    else:
        print(-1)

def size():
    print(len(sta))

def empty():
    if len(sta) != 0:
        print(0)
    else:
        print(1)

for i in range(n):
    order = sys.stdin.readline().rstrip()
    if "push" in order:
        push(order)
    elif order == "top":
        top()
    elif order == "size":
        size()
    elif order == "pop":
        pop()
    elif order == "empty":
        empty()