arr = [i for i in range(1, 10000)]
# print(arr)
self_num = []
for i in arr:
    if len(str(i)) == 1:
        a = i + i
        self_num.append(a)
        # print(i, a)
    elif len(str(i)) == 2:
        a = i + int(str(i)[0]) + int(str(i)[1])
    # a = i + int(i[0]) + int(i[1])
        self_num.append(a) 
        # print(i, a)
    elif len(str(i)) == 3:
        a = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
        self_num.append(a) 
        # print(i, a)
    else:
        a = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
        self_num.append(a)
# self_num.sort()
# print(self_num)
ans = list(set(arr) - set(self_num))
ans.sort()
for i in ans: print(i)
# print(type(i))
# a = "123456"
# a = ",".join(a)
# print(a)
