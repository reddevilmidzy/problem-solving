N = input()
count_number = 0
if len(N) == 1:
  N = "0"+N
a = N
while True:
  N = N[-1]+(str(int(N[0]) + int(N[1])))[-1]
  count_number += 1
  if N == a:
    print(count_number)
    break