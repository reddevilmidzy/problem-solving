zero = True
while zero:
  try:
    a, b = map(int, input().split())
    print(a+b)
  except EOFError:
    zero = False
