ip = list(input().split(':'))

if ip.count(''):
    while len(ip) > 8:
        del ip[ip.index('')]
    while len(ip) < 8:
        ip.insert(ip.index(''), '0000')

for i in range(8):
    if len(ip[i]) < 4:
        ip[i] = '0'*(4-len(ip[i])) + ip[i]

print(*ip, sep=':')