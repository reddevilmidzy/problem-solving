import sys
input = sys.stdin.readline
sevenseapirate = []
for i in range(int(input().rstrip())):
    sevenseapirate.append(float(input().rstrip()))

sevenseapirate.sort()
for j in range(7):
    print("{:.3f}".format(sevenseapirate[j]))