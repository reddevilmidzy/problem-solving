hour, min = map(int, input().split())
time = int(input())

if min + time < 60:
  print(hour, min+time)
elif min + time > 60:
  a = min + time
  hour = hour + a//60
  if hour >= 24:
    hour -= 24
    b = a % 60
    print(hour, b)
  else:
    print(hour, a%60)
else:
  if hour != 23:
    print(hour+1, 0)
  else:
    print(0,0)