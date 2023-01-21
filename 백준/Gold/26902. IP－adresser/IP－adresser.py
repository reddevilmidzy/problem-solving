ip = input()
n = len(ip)

def is_valid(num):
    return len((str(int(num)))) == len(str(num)) and int(num) < 256

res = 0

for i in range(1, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a,b,c,d, = ip[:i], ip[i:j], ip[j:k], ip[k:]
            if is_valid(a) and is_valid(b) and is_valid(c) and is_valid(d):
                res += 1
print(res)