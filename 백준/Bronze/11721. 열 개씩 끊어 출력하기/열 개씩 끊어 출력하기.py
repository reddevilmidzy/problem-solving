char = input()
for i in range(len(char)//10+1):
    print(char[i*10:i*10+10])