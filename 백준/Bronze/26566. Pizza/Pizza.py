import math
for _ in range(int(input())):
    a,p1 = map(int, input().split())
    r,p2 = map(int, input().split())
    r = r**2 * math.pi
    print(["Whole pizza", "Slice of pizza"][p1/a < p2/r])