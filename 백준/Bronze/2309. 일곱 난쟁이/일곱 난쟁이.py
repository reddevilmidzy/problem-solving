nano = [int(input()) for i in range(9)]
nano_sum = sum(nano)
for j in range(8):
    for k in range(j+1, 9):
        if nano_sum - (nano[j]+nano[k]) == 100:
            nano.remove(nano[k])
            nano.remove(nano[j])
            nano.sort()
            for o in sorted(nano):
                print(o)
            exit()